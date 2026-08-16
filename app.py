import streamlit as st
import urllib.request
import urllib.parse
import json

# Setup standard clean layout
st.set_page_config(page_title="Google", page_icon="🔍", layout="centered")

# Custom CSS for Pure Google UI Experience
st.markdown("""
<style>
    /* Clean white light background layout */
    .stApp {
        background-color: #ffffff;
        color: #202124;
        font-family: 'Roboto', arial, sans-serif;
    }
    
    /* Google Multi-Color Styled Logo Text */
    .google-logo-box {
        text-align: center;
        margin-top: 60px;
        margin-bottom: 25px;
        font-size: 5.5rem;
        font-weight: bold;
        font-family: 'Product Sans', 'Arial', sans-serif;
        letter-spacing: -2px;
    }
    .g-blue { color: #4285F4; }
    .g-red { color: #EA4335; }
    .g-yellow { color: #FBBC05; }
    .g-green { color: #34A853; }
    
    /* Clean minimalist subtitle label */
    .google-subtext {
        text-align: center;
        color: #70757a;
        font-size: 0.9rem;
        margin-top: -20px;
        margin-bottom: 30px;
    }
    
    /* Traditional Google Search Link Layouts */
    .google-card {
        background-color: #ffffff;
        padding: 5px 0px;
        margin-bottom: 26px;
        max-width: 652px;
    }
    
    /* Header layout for dynamic web favicon alignment */
    .card-header-layout {
        display: flex;
        align-items: center;
        gap: 12px;
        margin-bottom: 2px;
    }
    
    /* Website attribution domain styling */
    .google-meta-box {
        display: flex;
        flex-direction: column;
    }
    .google-display-name {
        color: #202124;
        font-size: 0.9rem;
        line-height: 1.3;
    }
    .google-url {
        color: #4d5156;
        font-size: 0.75rem;
        line-height: 1.3;
        word-break: break-all;
    }
    
    /* Micro Favicon Logo Settings */
    .favicon-logo {
        width: 26px;
        height: 26px;
        border-radius: 50%;
        background: #f1f3f4;
        padding: 4px;
        border: 1px solid #dadce0;
    }
    
    /* Classic Blue Hyperlinks */
    .google-link {
        font-size: 1.25rem;
        color: #1a0dab !important;
        text-decoration: none !important;
        display: inline-block;
        margin-top: 4px;
        margin-bottom: 4px;
    }
    .google-link:hover {
        text-decoration: underline !important;
    }
    
    /* Traditional grey snippet text */
    .google-desc {
        color: #4d5156;
        font-size: 0.9rem;
        line-height: 1.57;
        word-wrap: break-word;
    }
    
    /* Adjusting Streamlit native input search bar look to be pill-shaped */
    div[data-baseweb="input"] {
        border-radius: 24px !important;
        border: 1px solid #dadce0 !important;
        box-shadow: none !important;
        transition: box-shadow 0.2s;
    }
    div[data-baseweb="input"]:hover, div[data-baseweb="input"]:focus-within {
        box-shadow: 0 1px 6px rgba(32,33,36,0.28) !important;
        border-color: rgba(223,225,229,0) !important;
    }
    
    /* Hiding Streamlit structural framework buttons */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# Render Google Styled Multi-Color Header Component
st.markdown("""
<div class='google-logo-box'>
    <span class='g-blue'>G</span><span class='g-red'>o</span><span class='g-yellow'>o</span><span class='g-blue'>g</span><span class='g-green'>l</span><span class='g-red'>e</span>
</div>
<div class='google-subtext'>Custom Search Engine v4</div>
""", unsafe_allow_html=True)

# Clean Minimalist Search Input Field
query = st.text_input("Google Search", placeholder="Search the web or type a URL...", label_visibility="collapsed")

if query:
    st.write("") 
    with st.spinner("Searching..."):
        try:
            # High-speed decentralized SearXNG network processing layer
            encoded_query = urllib.parse.quote(query)
            api_url = f"https://searx.be{encoded_query}&format=json"
            
            req = urllib.request.Request(
                api_url, 
                headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
            )
            
            with urllib.request.urlopen(req) as response:
                data = json.loads(response.read().decode('utf-8'))
                results = data.get('results', [])

            # Extract up to top 8 traditional search entries
            min_length = min(len(results), 8)

            if min_length > 0:
                st.markdown(f"<p style='color: #70757a; font-size: 0.9rem; margin-bottom: 20px;'>About {min_length} results found</p>", unsafe_allow_html=True)
                st.write("---")
                
                for idx in range(min_length):
                    result = results[idx]
                    raw_url = result.get('url', '')
                    title_text = result.get('title', 'Untitled Entry')
                    desc_text = result.get('content', 'No context details available.')
                    
                    # Extract clean website name targets securely using urlparse
                    try:
                        parsed_uri = urllib.parse.urlparse(raw_url)
                        base_domain = f"{parsed_uri.scheme}://{parsed_uri.netloc}"
                        display_name = parsed_uri.netloc.replace("www.", "")
                    except Exception:
                        base_domain = raw_url
                        display_name = raw_url

                    # Pull high-resolution website favicons matching traditional google style
                    favicon_url = f"https://google.com{base_domain}"
                    
                    card_html = f"""
                    <div class="google-card">
                        <div class="card-header-layout">
                            <img class="favicon-logo" src="{favicon_url}" alt="site icon">
                            <div class="google-meta-box">
                                <span class="google-display-name">{display_name}</span>
                                <span class="google-url">{raw_url}</span>
                            </div>
                        </div>
                        <a class="google-link" href="{raw_url}" target="_blank">{title_text}</a>
                        <div class="google-desc">{desc_text}</div>
                    </div>
                    """
                    st.markdown(card_html, unsafe_allow_html=True)
            else:
                st.markdown("<p style='color:#202124; font-size:0.95rem;'>Your search did not match any documents.</p>", unsafe_allow_html=True)

        except Exception as e:
            st.markdown(f"<div style='color:#70757a; font-size:0.9rem;'>Network timeout. Please hit enter to try again. (Ref: {e})</div>", unsafe_allow_html=True)
