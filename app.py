import streamlit as st
import urllib.request
import json

# Setup webpage configuration for mobile and PC
st.set_page_config(page_title="Deep Search AI", page_icon="🔍", layout="centered")
st.title("🔍 Deep Search")

# Pull secret token safely
if "HF_TOKEN" not in st.secrets:
    st.error("Please configure your HF_TOKEN in the Streamlit Cloud dashboard settings.")
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

    # Generate response from Hugging Face Serverless Architecture
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        
        # Structure payload standard for Qwen
        api_url = "https://huggingface.co"
        headers = {
            "Authorization": f"Bearer {st.secrets['HF_TOKEN']}",
            "Content-Type": "application/json"
        }
        payload = {
            "inputs": prompt,
            "parameters": {"max_new_tokens": 512}
        }
        
        try:
            req = urllib.request.Request(api_url, data=json.dumps(payload).encode("utf-8"), headers=headers)
            with urllib.request.urlopen(req) as response:
                result = json.loads(response.read().decode("utf-8"))
                
                # Bulletproof text parsing for Hugging Face list outputs
                if isinstance(result, list) and len(result) > 0:
                    full_response = result[0].get("generated_text", "No text found.")
                elif isinstance(result, dict):
                    full_response = result.get("generated_text", str(result))
                else:
                    full_response = str(result)
                    
            message_placeholder.markdown(full_response)
        except Exception as e:
            full_response = f"Error processing response: {e}"
            message_placeholder.markdown(full_response)
            
    st.session_state.messages.append({"role": "assistant", "content": full_response})
