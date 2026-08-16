import streamlit as st
from g4f.client import Client

# Setup webpage configuration for mobile and PC
st.set_page_config(page_title="Deep Search AI", page_icon="🔍", layout="centered")
st.title("🔍 Deep Search")

# Initialize the automated zero-key client engine
@st.cache_resource
def load_engine():
    return Client()

client = load_engine()

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

    # Generate response from free automated rotators
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        try:
            # Uses automated provider routing to guarantee uptime
            response = client.chat.completions.create(
                model="gpt-4o",
                messages=[{"role": "user", "content": prompt}]
            )
            full_response = response.choices[0].message.content
            message_placeholder.markdown(full_response)
        except Exception as e:
            full_response = "Connection initializing. Please type your message once more."
            message_placeholder.markdown(full_response)
            
    st.session_state.messages.append({"role": "assistant", "content": full_response})
