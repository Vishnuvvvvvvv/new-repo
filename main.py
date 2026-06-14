import streamlit as st
import requests

# AMD Endpoint
API_URL = "https://c10a-4-31-212-69.ngrok-free.app/chat"

st.set_page_config(
    page_title="AMD Qwen Chat",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AMD Qwen Chat")
st.write("Running Qwen3-30B-A3B on AMD MI300X")

user_prompt = st.text_area(
    "Enter your prompt",
    height=150,
    placeholder="Ask anything..."
)

if st.button("Send", use_container_width=True):

    if not user_prompt.strip():
        st.warning("Please enter a prompt")
        st.stop()

    with st.spinner("Thinking..."):

        try:
            response = requests.post(
                API_URL,
                json={
                    "message": user_prompt
                },
                timeout=300
            )

            response.raise_for_status()

            result = response.json()

            st.subheader("Response")

            st.markdown(result["response"])

        except Exception as e:
            st.error(f"Error: {e}")