import streamlit as st
from duckduckgo_search import DDGS

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
    # Display user message
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Generate response from DuckDuckGo AI gateway (Meta-Llama 3.3 architecture)
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        try:
            with DDGS() as ddgs:
                # Calls the robust chat engine using llama model directly
                response = ddgs.chat(prompt, model="llama-3.3-70b")
                full_response = str(response)
            message_placeholder.markdown(full_response)
        except Exception as e:
            full_response = f"Initializing engine connection. Please press the arrow to resend. (Error: {e})"
            message_placeholder.markdown(full_response)
            
    st.session_state.messages.append({"role": "assistant", "content": full_response})
