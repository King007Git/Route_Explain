import streamlit as st 
from graph import route_explainer_agent

st.set_page_config(
    page_title="KT Bot",
    page_icon="🤖",
    layout="wide"
)

st.title("Route Explainer Bot")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

prompt = st.chat_input("Enter you query")
if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try: 
                response = route_explainer_agent.invoke({
                    "question": prompt
                })
                if isinstance(response, dict):
                    full_response = response.get("message", "Currently i do not have any explaination.")
            except Exception as e:
                st.error(f"Error calling agent: {e}")
                full_response = "Sorry, I encountered an error."
        st.markdown(full_response)
        if response.get('report'):
            st.markdown(response['report'])
    st.session_state.messages.append({"role": "assistant", "content": full_response})



