import streamlit as st
import time
from graph import route_explainer_agent  # Assuming this import is correct

st.set_page_config(
    page_title="KT Bot",
    page_icon="🤖",
    layout="wide"
)

st.title("KT Bot")
st.caption("capture, preserve, and operationalize decades of organizational and domain knowledge")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display existing chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Handle User Input
prompt = st.chat_input("Enter your query")
if prompt:
    # 1. Add User Message to History
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # 2. Generate Assistant Response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                response = route_explainer_agent.invoke({
                    "question": prompt
                })
            
                full_response = response.get("message", "Currently I do not have an explanation.")
                rationale = response.get("rationale", "No rationale provided.")
                report = response.get("report", None)

            except Exception as e:
                st.error(f"Error calling agent: {e}")
                full_response = "Sorry, I encountered an error."
                rationale = ""
                report = None

        # 3. Display the Main Response
        st.markdown(full_response)

        # 4. Display Report & Handle Download (If report exists)
        if report:
            st.markdown("---")
            st.markdown(report)
            
            # --- CREATE MARKDOWN CONTENT FOR DOWNLOAD ---
            markdown_content = f"""# 🤖 KT Bot Route Analysis

                **Date:** {time.strftime("%Y-%m-%d %H:%M:%S")}

                ## 1. AI Explanation
                {full_response}

                ---

                ## 2. Executive Report
                {report}

                ---

                ## 3. Technical Rationale (Raw Context)
                {rationale}
            """
            st.download_button(
                label="📥 Download Full Report (.md)",
                data=markdown_content,
                file_name=f"route_report_{int(time.time())}.md",
                mime="text/markdown"
            )
    st.session_state.messages.append({"role": "assistant", "content": full_response})