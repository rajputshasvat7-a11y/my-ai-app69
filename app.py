import streamlit as st
from duckduckgo_search import DDGS
from urllib.parse import urlparse

# Setup premium layout
st.set_page_config(page_title="Deep Search Engine // Cyber-Hub", page_icon="🎮", layout="wide")

# Custom CSS for Cyberpunk / Gaming Neon Interface
st.markdown("""
<style>
    /* Dark cyberpunk void background */
    .stApp {
        background: radial-gradient(circle at center, #0f0c1b 0%, #05020a 100%);
        color: #00ffcc;
        font-family: 'Segoe UI', Roboto, sans-serif;
    }
    
    /* Neon Glowing Title */
    .gaming-title {
        font-size: 3.5rem;
        font-weight: 900;
        text-align: center;
        text-transform: uppercase;
        letter-spacing: 4px;
        color: #fff;
        text-shadow: 0 0 10px #ff0055, 0 0 20px #ff0055, 0 0 40px #ff0055;
        margin-bottom: 2px;
    }
    .gaming-subtitle {
        text-align: center;
        color: #00ffcc;
        font-size: 1rem;
        text-transform: uppercase;
        letter-spacing: 2px;
        text-shadow: 0 0 8px rgba(0, 255, 204, 0.6);
        margin-bottom: 40px;
    }
    
    /* Cyber Gaming Results Cards */
    .gaming-card {
        background: rgba(15, 10, 30, 0.7);
        border: 2px solid #ff0055;
        border-radius: 8px;
        padding: 22px;
        margin-bottom: 22px;
        position: relative;
        overflow: hidden;
        box-shadow: 0 0 15px rgba(255, 0, 85, 0.2);
        transition: all 0.3s ease;
    }
    .gaming-card:hover {
        border-color: #00ffcc;
        box-shadow: 0 0 25px rgba(0, 255, 204, 0.4);
        transform: scale(1.01);
    }
    
    /* Header layout for dynamic web favicon alignment */
    .card-header-layout {
        display: flex;
        align-items: center;
        gap: 14px;
        margin-bottom: 8px;
    }
    
    /* Glowing dynamic logo image design */
    .favicon-logo {
        width: 28px;
        height: 28px;
        border-radius: 4px;
        background: #110b29;
        border: 1px solid #00ffcc;
        box-shadow: 0 0 8px rgba(0, 255, 204, 0.5);
    }
    
    /* Gaming Link Action Custom Elements */
    .gaming-link {
        font-size: 1.4rem;
        color: #fff !important;
        text-decoration: none !important;
        font-weight: 700;
        text-shadow: 0 0 5px rgba(255, 255, 255, 0.5);
    }
    .gaming-card:hover .gaming-link {
        color: #00ffcc !important;
        text-shadow: 0 0 8px rgba(0, 255, 204, 0.8);
    }
    
    .gaming-url {
        color: #ff0055;
        font-size: 0.85rem;
        margin-bottom: 12px;
        font-family: monospace;
    }
    .gaming-desc {
        color: #b3a7d6;
        font-size: 1rem;
        line-height: 1.6;
    }
    
    /* Remove native application container components */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# Render Cyberpunk Elements
st.markdown("<div class='gaming-title'>DEEP SEARCH</div>", unsafe_allow_html=True)
st.markdown("<div class='gaming-subtitle'>// SYSTEM STATUS: ONLINE // WEB SCRAPER V3</div>", unsafe_allow_html=True)

# Gaming Themed Input Field
query = st.text_input("QUERY_STRING", placeholder="ENTER TARGET KEYWORDS TO SCAN OBJECTIVES...", label_visibility="collapsed")

if query:
    st.write("") 
    with st.spinner("SCANNING THE QUANTUM WEB MATRICES..."):
        try:
            with DDGS() as ddgs:
                results = list(ddgs.text(query, region="wt-wt", max_results=8))

            if results:
                st.markdown(f"<p style='color: #ff0055; font-weight: bold;'>[+] TARGET MATCHES LOCATED: {len(results)}</p>", unsafe_allow_html=True)
                st.write("---")
                
                for idx, result in enumerate(results, 1):
                    # Automatically isolate base web domain to extract target icons
                    parsed_url = urlparse(result['href'])
                    base_domain = f"{parsed_url.scheme}://{parsed_url.netloc}"
                    
                    # Call Google's high-resolution global favicon extraction endpoint
                    favicon_url = f"https://google.com{base_domain}"
                    
                    card_html = f"""
                    <div class="gaming-card">
                        <div class="card-header-layout">
                            <img class="favicon-logo" src="{favicon_url}" alt="logo">
                            <a class="gaming-link" href="{result['href']}" target="_blank">{idx}. {result['title']}</a>
                        </div>
                        <div class="gaming-url">>> TARGET_URI: {result['href']}</div>
                        <div class="gaming-desc">{result['body']}</div>
                    </div>
                    """
                    st.markdown(card_html, unsafe_allow_html=True)
            else:
                st.markdown("<div style='border: 2px solid #ff0055; border-radius: 4px; padding: 15px; color: #ff0055; font-weight: bold; background: rgba(255,0,85,0.1);'>[-] SEARCH MATRIX EMPTY. TARGET UNRESOLVED.</div>", unsafe_allow_html=True)

        except Exception as e:
            st.error(f"NETWORK CRITICAL FAILURE: TERMINAL LINK DROPPED. (Details: {e})")
