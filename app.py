import streamlit as st
from google import genai

# Setup webpage configuration for mobile and PC
st.set_page_config(page_title="Deep Search AI", page_icon="🔍", layout="centered")
st.title("🔍 Deep Search")

# Initialize Gemini Client safely using Streamlit Secrets
try:
    client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])
except Exception:
    st.error("Please configure your GEMINI_API_KEY in the Streamlit Cloud dashboard settings.")
    st.stop()

# Initialize chat history in session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display past chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("Ask Deep Search anything..."):
    # Display user message
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Generate response from Gemini
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        try:
            # Using the production-ready active flash model
            response = client.models.generate_content(
                model='gemini-3.7-flash',
                contents=prompt,
            )
            full_response = response.text
            message_placeholder.markdown(full_response)
        except Exception as e:
            full_response = f"Error generating response: {e}"
            message_placeholder.markdown(full_response)
            
    st.session_state.messages.append({"role": "assistant", "content": full_response})
