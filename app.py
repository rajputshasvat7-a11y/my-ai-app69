import streamlit as st
import urllib.request
import urllib.parse
import json
import re

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
            # Bulletproof, dependency-free direct HTTP networking layer
            encoded_query = urllib.parse.quote(query)
            api_url = f"https://duckduckgo.com{encoded_query}"
            
            req = urllib.request.Request(
                api_url, 
                headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
            )
            
            with urllib.request.urlopen(req) as response:
                html_content = response.read().decode('utf-8')
            
            # Extract matches using clean pattern matching
            links = re.findall(r'<a class="result__url"[^>]*href="([^"]+)"', html_content)
            titles = re.findall(r'<a class="result__snippet"[^>]*href="[^"]+">([^<]+)</a>', html_content)
            snippets = re.findall(r'<td class="result__snippet">([^<]+)</td>', html_content)
            
            # Fallback patterns to capture varying structure configurations
            if not links:
                links = re.findall(r'href="([^"]+)" class="links_main__href"', html_content)
                titles = re.findall(r'class="links_main__href">([^<]+)</a>', html_content)
                snippets = re.findall(r'class="links_main__snippet">([^<]+)</div>', html_content)

            # Standardize sizes across parsed structures
            min_length = min(len(links), len(titles), len(snippets), 8)

            if min_length > 0:
                st.markdown(f"<p style='color: #ff0055; font-weight: bold;'>[+] TARGET MATCHES LOCATED: {min_length}</p>", unsafe_allow_html=True)
                st.write("---")
                
                for idx in range(min_length):
                    raw_url = links[idx]
                    # Parse out proxy nesting parameters if existing
                    if "uddg=" in raw_url:
                        raw_url = urllib.parse.unquote(raw_url.split("uddg=")[1].split("&")[0])
                    
                    title_text = titles[idx].strip()
                    desc_text = snippets[idx].strip()
                    
                    # Isolate clean domain base targets
                    try:
                        domain_parts = raw_url.split("//")[1].split("/")[0]
                        base_domain = f"https://{domain_parts}"
                    except Exception:
                        base_domain = raw_url

                    # Pull high-resolution logos automatically
                    favicon_url = f"https://google.com{base_domain}"
                    
                    card_html = f"""
                    <div class="gaming-card">
                        <div class="card-header-layout">
                            <img class="favicon-logo" src="{favicon_url}" alt="logo">
                            <a class="gaming-link" href="{raw_url}" target="_blank">{idx + 1}. {title_text}</a>
                        </div>
                        <div class="gaming-url">>> TARGET_URI: {raw_url}</div>
                        <div class="gaming-desc">{desc_text}</div>
                    </div>
                    """
                    st.markdown(card_html, unsafe_allow_html=True)
            else:
                st.markdown("<div style='border: 2px solid #ff0055; border-radius: 4px; padding: 15px; color: #ff0055; font-weight: bold; background: rgba(255,0,85,0.1);'>[-] SEARCH MATRIX EMPTY. TARGET UNRESOLVED.</div>", unsafe_allow_html=True)

        except Exception as e:
            st.markdown(f"<div style='color:#ff0055;'>NETWORK FAILURE: {e}</div>", unsafe_allow_html=True)
