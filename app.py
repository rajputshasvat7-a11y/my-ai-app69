import streamlit as st
from duckduckgo_search import DDGS

# Setup premium wide layout
st.set_page_config(page_title="Deep Search Engine", page_icon="🔍", layout="wide")

# Custom CSS for Modern Premium Dark UI
st.markdown("""
<style>
    /* Main app background color */
    .stApp {
        background: linear-gradient(135deg, #0d1117 0%, #161b22 100%);
        color: #c9d1d9;
    }
    
    /* Center Title and styling */
    .search-title {
        font-family: 'Inter', sans-serif;
        font-size: 3rem;
        font-weight: 800;
        text-align: center;
        background: linear-gradient(45deg, #58a6ff, #bc8cff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 5px;
    }
    .search-subtitle {
        text-align: center;
        color: #8b949e;
        font-size: 1.1rem;
        margin-bottom: 40px;
    }
    
    /* Custom Stylized Cards for Search Results */
    .result-card {
        background-color: #21262d;
        border: 1px solid #30363d;
        border-radius: 12px;
        padding: 20px;
        margin-bottom: 20px;
        transition: transform 0.2s, border-color 0.2s;
        box-shadow: 0 4px 12px rgba(0,0,0,0.15);
    }
    .result-card:hover {
        transform: translateY(-2px);
        border-color: #58a6ff;
        box-shadow: 0 6px 16px rgba(88, 166, 255, 0.1);
    }
    
    /* Result Link Styling */
    .result-title-link {
        font-size: 1.4rem;
        color: #58a6ff !important;
        text-decoration: none !important;
        font-weight: 600;
    }
    .result-title-link:hover {
        color: #79c0ff !important;
        text-decoration: underline !important;
    }
    .result-url {
        color: #3ee295;
        font-size: 0.85rem;
        margin-top: 3px;
        margin-bottom: 12px;
        word-break: break-all;
    }
    .result-snippet {
        color: #e6edf3;
        font-size: 1rem;
        line-height: 1.5;
    }
    
    /* Hiding Streamlit structural clutter for premium app feel */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# Render Redesigned Headers
st.markdown("<div class='search-title'>🔍 Deep Search</div>", unsafe_allow_html=True)
st.markdown("<div class='search-subtitle'>Next-generation instant web intelligence platform</div>", unsafe_allow_html=True)

# Main Centralized Search Bar
query = st.text_input("Search keywords", placeholder="Type keywords to search the live web...", label_visibility="collapsed")

if query:
    st.write("") # Spacer
    with st.spinner("Analyzing web entries..."):
        try:
            with DDGS() as ddgs:
                results = list(ddgs.text(query, region="wt-wt", max_results=8))

            if results:
                st.markdown(f"<p style='color: #8b949e;'>Showing top <b>{len(results)}</b> direct intelligence matches:</p>", unsafe_allow_html=True)
                st.write("---")
                
                # Render results inside custom HTML CSS Premium Cards
                for idx, result in enumerate(results, 1):
                    card_html = f"""
                    <div class="result-card">
                        <a class="result-title-link" href="{result['href']}" target="_blank">{idx}. {result['title']}</a>
                        <div class="result-url">{result['href']}</div>
                        <div class="result-snippet">{result['body']}</div>
                    </div>
                    """
                    st.markdown(card_html, unsafe_allow_html=True)
            else:
                st.markdown("<div style='background-color: #2d1e1f; border: 1px solid #f85149; border-radius: 8px; padding: 15px; color: #f85149;'>No direct intelligence matches located. Refine your query.</div>", unsafe_allow_html=True)

        except Exception as e:
            st.error(f"Engine connection timed out. Please try hitting enter again. (Details: {e})")
