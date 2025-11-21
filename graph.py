from db import DATA

# from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field
from langgraph.graph import StateGraph, START, END
from typing import List
from typing_extensions import TypedDict, NotRequired, Optional
from dotenv import load_dotenv
import json
import os
import httpx

load_dotenv()

base_url = os.getenv("api_endpoint")
api_key = os.getenv("api_key")
client = httpx.Client(verify=False)

llm = ChatOpenAI(
    base_url=base_url,
    model="azure/genailab-maas-gpt-4o", # copy from the .env
    api_key=api_key,
    http_client=client  
)

# llm = ChatGoogleGenerativeAI(
#     model="gemini-2.5-flash",
#     temperature=0.7,
#     max_retries=2,
# )

class AgentState(TypedDict):
    question: str
    message: str
    end: bool = False
    route_id: str
    route_data: str
    rationale: NotRequired[str]
    report: str

def fetch_from_data(target_route_id):
    for i in DATA:
        for route in i.get("routes", []):
            if route.get("route_id").lower() == target_route_id.lower():
                route['created_date'] = i['date']
                return json.dumps(route, indent=2)
    return None

class RouteIDOutput(BaseModel):
    route_id: Optional[str] = Field(
        default=None,
        description="Extract Route ID (e.g., R1, R2). If no Route ID is found in the context, strictly return null."
    )
routeid_llm = llm.with_structured_output(RouteIDOutput)
def routeid_node(state: AgentState) -> AgentState:
    question = state["question"]
    system = "You are an extraction agent. Extract the route ID from the user query."
    
    result = routeid_llm.invoke([
        {"role": "system", "content": system},
        {"role": "user", "content": question}
    ])
    return {
        "route_id": result.route_id 
    }
def build_routeid_graph():
    builder = StateGraph(AgentState)
    builder.add_node("classify_intent", routeid_node)
    builder.add_edge(START, "classify_intent")
    builder.add_edge("classify_intent", END)
    return builder.compile()

def retrieval_node(state: AgentState) -> AgentState:
    r_id = state.get("route_id", None)
    if not r_id:
        return {"message": "Please mention the route ID you want to get information about?", "end":True}
    data = fetch_from_data(r_id)
    if not data:
        return {"message": "sorry not able to fetch the data......", "end":True}
    return {"route_data": fetch_from_data(r_id)}
def build_retrieval_graph():
    builder = StateGraph(AgentState)
    builder.add_node("retrieve", retrieval_node)
    builder.add_edge(START, "retrieve")
    builder.add_edge("retrieve", END)
    return builder.compile()
def rationale_node(state: AgentState) -> AgentState:
    end = state.get("end", False)
    if end:
        return {}
    Route_Data_Json = state.get('route_data', None)
    system = (
        """
            You are a professional travel route explainer for logistics operations.
            
            You will receive a JSON object describing one or more vehicle routes for a given day. Your job is to explain the route(s) in clear, friendly, easy-to-understand natural language so that a non-technical person (like a driver, dispatcher, or customer) can understand:
            
            - The overall plan for the day
            - The total travel time and distance
            - The sequence of stops for each vehicle
            - What happens at each stop (pickup / delivery / break / depot)
            - How vehicle capacity and driver constraints are respected
            
            GENERAL RULES
            - Always preserve the numbers and ordering from the JSON. Do NOT change distances, times, or sequence of stops.
            - Do not invent new stops, times, or locations that are not present in the JSON.
            - Use simple, concise language. Avoid heavy jargon or formulas.
            - Use bullet points or short sections to keep the explanation readable.
            - If there are multiple vehicles, clearly separate the explanation per vehicle.
            - If any constraints are tight (e.g. near capacity or time windows almost violated), briefly point this out.
            
            JSON STRUCTURE (TYPICAL EXAMPLE)
            You will usually receive JSON similar to this shape (field names may vary slightly):
            
            {
              "date": "2025-11-22",
              "routes": [
                {
                  "route_id": "R1",
                  "vehicle": {
                    "id": "V1",
                    "type": "Van",
                    "capacity_kg": 1200
                  },
                  "driver": {
                    "id": "D1",
                    "name": "Alex",
                    "max_work_minutes": 480,
                    "performance": {
                      "speed_factor": 0.95
                    }
                  },
                  "summary": {
                    "total_distance_km": 76.3,
                    "total_travel_time_min": 142,
                    "total_service_time_min": 70,
                    "total_stops": 6
                  },
                  "stops": [
                    {
                      "sequence": 1,
                      "stop_id": "S0",
                      "type": "depot",
                      "name": "Main Depot",
                      "address": "12 Warehouse Road",
                      "planned_arrival": "2025-11-22T08:00:00+05:30",
                      "planned_departure": "2025-11-22T08:15:00+05:30",
                      "distance_from_previous_km": 0,
                      "travel_time_from_previous_min": 0,
                      "service_time_min": 15,
                      "load_change_kg": 900,
                      "load_after_stop_kg": 900,
                      "time_window": { "start": "08:00", "end": "09:00" }
                    },
                    ...
                  ]
                },
                ...
              ]
            }
            
            OUTPUT STYLE
            1. Start with a short overview of the day:
               - Mention the date.
               - Mention how many vehicles and how many total stops.
               - Mention approximate total distance and total driving time if available.
            
            2. For each route (each vehicle):
               - Give a brief summary:
                 - Vehicle type, driver name.
                 - Total distance, total driving time, number of stops.
                 - Peak load vs vehicle capacity, if provided.
               - Then walk through the stops in order using bullet points or numbered steps.
                 For each stop, describe:
                   - Where the stop is (name and address).
                   - What time the driver is expected to arrive and leave (in local time).
                   - What happens there:
                     - Depot load/unload
                     - Customer delivery (how much is delivered)
                     - Customer pickup (how much is picked up)
                     - Driver break (how long)
                   - How the vehicle load changes (if load fields are provided).
                   - Any time-window information (“We are scheduled within the customer’s requested time window of 10:00–12:00”).
            
            3. Constraints and performance:
               - If the route is close to capacity or close to the maximum working time, mention this gently as a note.
               - If you see long gaps or waiting times due to time windows, explain them in simple terms (e.g. “The driver arrives early and waits 10 minutes for the time window to open.”).
            
            4. Error handling:
               - If important fields are missing, explain the route as well as you can based on what is available.
               - If the JSON is empty or invalid, say that you cannot describe the route and state what is missing.
            
            Never output code or JSON in your final explanation unless explicitly requested. Focus on a clear, human-friendly description.

        """
    )
    res = llm.invoke(
    [
        {"role": "system", "content": system},
        {"role": "user", "content": f"Route Data JSON:\n{Route_Data_Json}"},
    ]
    )
    return {"rationale":res.content}

def build_rationale_graph():
    builder = StateGraph(AgentState)
    builder.add_node("expert_rationale", rationale_node)
    builder.add_edge(START, "expert_rationale")
    builder.add_edge("expert_rationale", END)
    return builder.compile()

def route_flow(state: AgentState) -> AgentState:
    end = state.get("end", False)
    if end:
        return {}
    rationale = state.get('rationale', "Failed to fetch the Route Rational......")
    system  = (
        """
        You are a Route Visualization Expert. Your goal is to convert detailed text-based route plans into a structured, vertical "Text Flow Diagram".
        
        **Strict Formatting Rules:**
        1.  **Output Wrapper:** You MUST enclose the entire output within a markdown code block labeled `{flow}`. 
            Example:
            ``` {flow}
            (Diagram content here)
            ```
        2.  **Layout:** Use a vertical timeline format. Align time, icons, and location names neatly.
        3.  **Connectors:** Use vertical lines (`|`) and arrows (`↓` or `v`) to show movement between stops.
        
        **Content Guidelines:**
        1.  **Icons:** Use these specific emojis:
            * Depot: 🏢
            * Delivery: 📦
            * Pickup: 📤
            * Break: ☕
        2.  **Node Details:** [Time] [Icon] [Location Name] (Load: [X]kg)
        3.  **Edge Details:** On the vertical lines between nodes, display the [Travel Time] and [Distance].
        
        **Output Template:**
        ``` {flow}
        [Arrival Time] [Icon] [Location Name] (Load: [Current Load]kg)
              |
              | [Travel Time] / [Distance]
              ↓
        [Next Arrival Time] [Icon] [Next Location]...
        """
    )
    res = llm.invoke(
    [
        {"role": "system", "content": system},
        {"role": "user", "content": f"Route Text:\n{rationale}"},
    ]
    )
    return {"report":res.content}
def build_report_graph():
    builder = StateGraph(AgentState)
    builder.add_node("route_flow", route_flow)
    builder.add_edge(START, "route_flow")
    builder.add_edge("route_flow", END)
    return builder.compile()
def generate_message(state: AgentState) -> AgentState:
    end = state.get("end", False)
    if end:
        return {}
    rationale = state.get('rationale', "Failed to fetch the Route Rational......")
    system = (
        """
        You are a Senior Logistics Analyst. Your task is to review raw route data and generate a "Route Performance Executive Summary."
        
        **Guidelines:**
        1.  **Tone:** Professional, concise, and data-driven.
        2.  **Structure:**
            * **Route Header:** ID, Date, Driver, Vehicle.
            * **Efficiency Metrics:** Calculate and display utilization (Load % and Time).
            * **Operational Overview:** A 2-sentence summary of the route's purpose.
            * **Constraint Check:** Explicitly state if time windows and capacity limits were met (Pass/Fail).
            * **Key Timeline Milestones:** Only list the Start Time, End Time, and Break Time. Do not list every stop.
        
        **Output Format:**
        ## 📊 Executive Route Report: [Route ID]
        **Status:** [Scheduled/Completed]
        
        **1. Key Metrics**
        * **Capacity Utilization:** [Peak Load / Max Capacity]%
        * **Total Distance:** [Value] km
        * **Total Duration:** [Value] min
        
        **2. Operational Analysis**
        [Provide a brief paragraph summarizing the route's flow, e.g., "The route begins at X, services Y customers, includes a pickup at Z, and returns to depot."]
        
        **3. Compliance & Constraints**
        * ✅ Time Windows: [Met/Missed]
        * ✅ Vehicle Capacity: [Within Limits/Overload]
        * ✅ Driver Break: [Taken/Skipped]
        """
    )
    res = llm.invoke(
    [
        {"role": "system", "content": system},
        {"role": "user", "content": f"Route Text:\n{rationale}"},
    ]
    )
    return {"message":res.content}
def build_message_graph():
    builder = StateGraph(AgentState)
    builder.add_node("generate_res", generate_message)
    builder.add_edge(START, "generate_res")
    builder.add_edge("generate_res", END)
    return builder.compile()

route_id_agent = build_routeid_graph()
retrieval_agent = build_retrieval_graph()
rationale_agent = build_rationale_graph()
report_agent = build_report_graph()
res_graph = build_message_graph()

def build_master_route_graph():
    builder = StateGraph(AgentState)
    builder.add_node("route_id_agent", route_id_agent)
    builder.add_node("retrieval_agent", retrieval_agent)
    builder.add_node("rationale_agent", rationale_agent)
    builder.add_node("report_agent", report_agent)
    builder.add_node("res_graph",res_graph)
    builder.add_edge(START, "route_id_agent")
    builder.add_edge("route_id_agent", "retrieval_agent")
    builder.add_edge("retrieval_agent", "rationale_agent")
    builder.add_edge("rationale_agent", "report_agent")
    builder.add_edge("report_agent", "res_graph")
    builder.add_edge("res_graph", END)
    return builder.compile()

route_explainer_agent = build_master_route_graph()