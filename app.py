import streamlit as st
from duckduckgo_search import DDGS

# Setup webpage configuration for mobile and PC
st.set_page_config(page_title="Deep Search Engine", page_icon="🔍", layout="wide")

# App title headers visible to users
st.markdown("<h1 style='text-align: center;'>🔍 Deep Search Engine</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: gray;'>Search the live web directly from mobile or PC</p>", unsafe_allow_html=True)

# Main open search input bar
query = st.text_input("Enter search keywords", placeholder="Search the web or type a URL...", label_visibility="collapsed")

if query:
    with st.spinner(f"Searching the live web for '{query}'..."):
        try:
            # Pure synchronous execution layout for instant data fetches
            with DDGS() as ddgs:
                results = list(ddgs.text(query, max_results=8))

            if results:
                st.success(f"Found {len(results)} live matches:")
                st.write("---")
                
                # Display results beautifully with clean layout structures
                for idx, result in enumerate(results, 1):
                    st.markdown(f"### {idx}. [{result['title']}]({result['href']})")
                    st.markdown(f"*{result['href']}*")
                    st.info(result['body'])
                    st.write("")
            else:
                st.warning("No search matches found. Try different keywords.")

        except Exception as e:
            st.error(f"Engine connection timed out. Please try hitting enter again. (Error: {e})")
