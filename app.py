import streamlit as st
import urllib.request
import json

# Setup webpage configuration for mobile and PC
st.set_page_config(page_title="Deep Search AI", page_icon="🔍", layout="centered")
st.title("🔍 Deep Search")

# Initialize chat history in session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display past chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("Ask Deep Search anything..."):
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        
        # Pointing to the stable open-access platform server
        api_url = "https://openrouter.ai"
        headers = {
            "Content-Type": "application/json",
            "HTTP-Referer": "https://streamlit.io", 
            "X-Title": "Deep Search App"
        }
        payload = {
            "model": "meta-llama/llama-3.2-3b-instruct:free",
            "messages": [{"role": "user", "content": prompt}]
        }
        
        try:
            req = urllib.request.Request(api_url, data=json.dumps(payload).encode("utf-8"), headers=headers)
            with urllib.request.urlopen(req) as response:
                result = json.loads(response.read().decode("utf-8"))
                full_response = result["choices"][0]["message"]["content"]
            message_placeholder.markdown(full_response)
        except Exception as e:
            full_response = f"Connection refreshed. Please hit the arrow button to resend your message. (Ref: {e})"
            message_placeholder.markdown(full_response)
            
    st.session_state.messages.append({"role": "assistant", "content": full_response})
