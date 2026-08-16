import streamlit as st
from duckduckgo_search import DDGS
import urllib.request
import urllib.parse
import json

# Setup webpage configuration for mobile and PC
st.set_page_config(page_title="Deep Search Engine", page_icon="🔍", layout="wide")

# Check if environment variables are fully ready
if "GOOGLE_CLIENT_ID" not in st.secrets or "GOOGLE_CLIENT_SECRET" not in st.secrets:
    st.error("Authentication variables missing inside Streamlit Secrets settings panel.")
    st.stop()

# Helper function to trade authorization code for user identity info
def get_logged_in_user_email():
    query_params = st.query_params
    if "code" not in query_params:
        return None
    
    code = query_params["code"]
    token_url = "https://googleapis.com"
    
    # Domain configuration for the secure callback target
    redirect_uri = "https://streamlit.app"
    
    data = urllib.parse.urlencode({
        "code": code,
        "client_id": st.secrets["GOOGLE_CLIENT_ID"],
        "client_secret": st.secrets["GOOGLE_CLIENT_SECRET"],
        "redirect_uri": redirect_uri,
        "grant_type": "authorization_code"
    }).encode("utf-8")
    
    try:
        req = urllib.request.Request(token_url, data=data, headers={"Content-Type": "application/x-www-form-urlencoded"})
        with urllib.request.urlopen(req) as response:
            res_data = json.loads(response.read().decode("utf-8"))
            access_token = res_data.get("access_token")
            
        # Call userinfo endpoint using token access
        info_url = f"https://googleapis.com{access_token}"
        with urllib.request.urlopen(info_url) as info_response:
            user_info = json.loads(info_response.read().decode("utf-8"))
            return user_info.get("email")
    except Exception:
        return None

# Manage user session tracking
if "user_email" not in st.session_state:
    st.session_state.user_email = get_logged_in_user_email()

# Enforce Security Barrier Gate
if not st.session_state.user_email:
    st.markdown("<h2 style='text-align: center;'>🔐 Access Protected</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>Please authenticate with your approved Google account to open Deep Search Engine.</p>", unsafe_allow_html=True)
    
    # Generate Google Authorization URL Endpoint
    redirect_uri = "https://streamlit.app"
    auth_url = (
        "https://google.com?"
        "response_type=code&"
        f"client_id={st.secrets['GOOGLE_CLIENT_ID']}&"
        f"redirect_uri={redirect_uri}&"
        "scope=openid%20email&"
        "prompt=select_account"
    )
    
    # Native Streamlit button layout to handle safe redirection
    if st.button("Sign in with Google", type="primary"):
        st.markdown(f'<meta http-equiv="refresh" content="0; url={auth_url}">', unsafe_allow_html=True)
    st.stop()

# Email Restriction Verification Layer
if st.session_state.user_email != st.secrets["ALLOWED_EMAIL"]:
    st.error(f"Access Denied: The account '{st.session_state.user_email}' is not permitted to view this system.")
    if st.button("Log out"):
        st.session_state.clear()
        st.query_params.clear()
        st.rerun()
    st.stop()

# --- Main App Execution Logic ---
st.sidebar.success(f"Authenticated: {st.session_state.user_email}")
if st.sidebar.button("Sign Out"):
    st.session_state.clear()
    st.query_params.clear()
    st.rerun()

st.markdown("<h1 style='text-align: center;'>🔍 Deep Search Engine</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: gray;'>Search the live web directly from mobile or PC</p>", unsafe_allow_html=True)

query = st.text_input("Enter search keywords", placeholder="Search the web or type a URL...", label_visibility="collapsed")

if query:
    with st.spinner(f"Searching the live web for '{query}'..."):
        try:
            with DDGS() as ddgs:
                results = list(ddgs.text(query, max_results=8))

            if results:
                st.success(f"Found {len(results)} live matches:")
                st.write("---")
                
                for idx, result in enumerate(results, 1):
                    st.markdown(f"### {idx}. [{result['title']}]({result['href']})")
                    st.markdown(f"*{result['href']}*")
                    st.info(result['body'])
                    st.write("")
            else:
                st.warning("No search matches found. Try different keywords.")
        except Exception as e:
            st.error(f"Engine connection timed out. Please try hitting enter again. (Error: {e})")
