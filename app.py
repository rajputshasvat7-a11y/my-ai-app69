import streamlit as st
from duckduckgo_search import DDGS

# Setup webpage configuration for mobile and PC
st.set_page_config(page_title="Deep Search Engine", page_icon="🔍", layout="wide")

# Streamlit native single-line login mechanism
if not st.experimental_user.is_logged_in:
    st.markdown("<h2 style='text-align: center;'>🔐 Access Protected</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>Please authenticate with your approved Google account to open Deep Search Engine.</p>", unsafe_allow_html=True)
    
    # Official built-in layout handler
    if st.button("Sign in with Google", type="primary", use_container_width=True):
        st.login("google")
    st.stop()

# --- Main App Execution Logic ---
st.sidebar.success(f"Authenticated: {st.experimental_user.email}")
if st.sidebar.button("Sign Out"):
    st.logout()
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
