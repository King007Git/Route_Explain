import streamlit as st
import time
from graph import route_explainer_agent
import utils

st.set_page_config(
    page_title="KT Bot",
    page_icon="🤖",
    layout="wide"
)

st.title("Route Explain Bot")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

prompt = st.chat_input("Enter your query")

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                response = route_explainer_agent.invoke({"question": prompt})
                full_response = response.get("message", "No explanation available.")
                rationale = response.get("rationale", "No rationale provided.")
                report = response.get("report", None)

            except Exception as e:
                st.error(f"Error calling agent: {e}")
                full_response = "Sorry, I encountered an error."
                rationale = ""
                report = None

        st.markdown(full_response)
        if report:
            st.markdown("---")
            st.markdown(report)
            
            md_content = utils.generate_report_string(full_response, report, rationale)
            pdf_bytes = utils.convert_markdown_to_pdf(md_content)
            
            file_ts = int(time.time())
            
            col1, col2 = st.columns([1, 4])
            
            if pdf_bytes:
                with col1:
                    st.download_button(
                        label="📥 Download PDF",
                        data=pdf_bytes,
                        file_name=f"route_report_{file_ts}.pdf",
                        mime="application/pdf"
                    )
            else:
                with col1:
                    st.warning("PDF generation failed.")
            with col2:
                st.download_button(
                    label="📄 Download Source (MD)",
                    data=md_content,
                    file_name=f"route_report_{file_ts}.md",
                    mime="text/markdown"
                )

    st.session_state.messages.append({"role": "assistant", "content": full_response})