import streamlit as st
import google.generativeai as genai

# Setup webpage configuration for mobile and PC
st.set_page_config(page_title="AI Chatbot", page_icon="🤖", layout="centered")
st.title("💬 Deep Search")

# Initialize Gemini Client safely using Streamlit Secrets
try:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
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
if prompt := st.chat_input("Type your message here..."):
    # Display user message
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Generate response from Gemini
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        try:
            model = genai.GenerativeModel("gemini-1.5-flash")
            response = model.generate_content(prompt)
            full_response = response.text
            message_placeholder.markdown(full_response)
        except Exception as e:
            full_response = f"Error generating response: {e}"
            message_placeholder.markdown(full_response)
            
    st.session_state.messages.append({"role": "assistant", "content": full_response})
