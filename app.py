import streamlit as str
from google import genai

# Setup page configuration for mobile and PC
str.set_page_config(page_title="AI Chatbot", page_icon="🤖", layout="centered")
str.title("💬 My Personal AI Chatbot")

# Initialize Gemini Client (Ensure GEMINI_API_KEY is set in your environment variables)
# Alternatively, replace with genai.Client(api_key="YOUR_ACTUAL_API_KEY") for local testing
try:
    client = genai.Client()
except Exception:
    str.error("Please configure your Gemini API key.")
    str.stop()

# Initialize chat history in session state
if "messages" not in str.session_state:
    str.session_state.messages = []

# Display past chat messages
for message in str.session_state.messages:
    with str.chat_message(message["role"]):
        str.markdown(message["content"])

# React to user input
if prompt := str.chat_input("Type your message here..."):
    # Display user message
    str.chat_message("user").markdown(prompt)
    str.session_state.messages.append({"role": "user", "content": prompt})

    # Generate response from Gemini 2.5 Flash
    with str.chat_message("assistant"):
        message_placeholder = str.empty()
        full_response = ""
        
        try:
            # Use gemini-2.5-flash for fast, responsive text generation
            response = client.models.generate_content(
                model='gemini-2.5-flash',
                contents=prompt,
            )
            full_response = response.text
            message_placeholder.markdown(full_response)
                    except Exception as e:
            full_response = f"Error generating response: {e}"
            message_placeholder.markdown(full_response)

            
    str.session_state.messages.append({"role": "assistant", "content": full_response})
