import streamlit as st
import zipfile
from google import genai

# Setup simple clean centered layout
st.set_page_config(page_title="Deep Search AI", page_icon="🔍", layout="centered")

# Try to look for the zip folder and extract the APK file out of it on the fly
apk_data = None
try:
    with zipfile.ZipFile("Deep Search 1.0.zip", "r") as z:
        for filename in z.namelist():
            if filename.endswith(".apk"):
                with z.open(filename) as f:
                    apk_data = f.read()
                break
except Exception:
    try:
        with open("Deep Search 1.0.zip", "rb") as file:
            apk_data = file.read()
    except Exception:
        apk_data = None

# Main Screen App Header
st.title("🔍 Deep Search AI")
st.write("Powered by Google GenAI Hub Architecture.")

# Main Screen Download Button Layout Placement
if apk_data:
    st.download_button(
        label="📥 Download Standalone Android APK",
        data=apk_data,
        file_name="Deep_Search.apk",
        mime="application/vnd.android.package-archive",
        type="primary",
        use_container_width=True
    )
    st.write("") 
else:
    st.info("💡 Note: Please ensure your uploaded zip file is named exactly 'Deep Search 1.0.zip' inside your GitHub repository folder to unlock the download button.")

st.write("---")

# Initialize Gemini Client safely using Streamlit Secrets panel configurations
try:
    client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])
except Exception:
    st.error("Missing Security Credentials: Go to your Streamlit dashboard Settings -> Secrets and define your key format: GEMINI_API_KEY = 'your_key'")
    st.stop()

# Initialize chat history state arrays natively inside session storage properties
if "messages" not in st.session_state:
    st.session_state.messages = []

# Continuously display existing multi-turn chat text streams
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to fresh user conversational inputs
if prompt := st.chat_input("Ask Deep Search AI anything..."):
    # Display user input layout card
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Call official high-speed stable Gemini production model infrastructure
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        try:
            response = client.models.generate_content(
                model='gemini-2.5-flash',
                contents=prompt,
            )
            full_response = response.text
            message_placeholder.markdown(full_response)
        except Exception as e:
            full_response = f"AI Node dropped context request parameter execution. (Details: {e})"
            message_placeholder.markdown(full_response)
            
    st.session_state.messages.append({"role": "assistant", "content": full_response})
