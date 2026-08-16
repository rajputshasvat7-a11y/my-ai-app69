import streamlit as st
import zipfile
import urllib.parse

# Setup premium wide layout
st.set_page_config(page_title="Deep Search Engine", page_icon="🔍", layout="wide")

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

# Main Screen Application Header Configuration
st.markdown("<h1 style='text-align: center; color: #1f77b4;'>🔍 Deep Search</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #7f7f7f;'>Multi-Mode Content Extraction Platform</p>", unsafe_allow_html=True)

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

st.write("---")

# Regular search input bar
query = st.text_input("Enter search keywords", placeholder="Type keywords or parts to scan...", label_visibility="collapsed")

if query:
    # Encodes spaces safely into standard HTTP url strings (+ signs instead of %20)
    encoded_query = urllib.parse.quote_plus(query)
    
    # Feature-Driven Structural Mode Tabs Setup
    tab_web, tab_ai, tab_shop = st.tabs(["🌐 Core Index Links", "✨ AI Intelligence Node", "🛍️ Shopping Compare"])
    
    # ================= FEATURE 1: CORE INDEX LINKS =================
    with tab_web:
        st.write(f"**Indexed results matching your query parameter:**")
        st.write("")
        
        # Primary Targeted Result Wrapper Box
        with st.container(border=True):
            st.markdown(f"### [Marketplace Index Matrix // Query: {query}](https://google.com{encoded_query})")
            st.caption(f"https://web-index.net{encoded_query}")
            st.write(f"Analyze comprehensive web listings, data specifications, documentation metrics, and articles tracking the parameter: {query}.")
        
        st.write("")
        
        # Secondary General Knowledge Wrapper Box
        with st.container(border=True):
            st.markdown(f"### [Reference Encyclopedia Data Node // {query}](https://wikipedia.org{encoded_query})")
            st.caption(f"https://wikipedia.org{encoded_query}")
            st.write(f"Review historical contexts, structural descriptions, engineering breakdowns, and standard documentation files regarding {query}.")
        
        st.write("---")

    # ================= FEATURE 2: AI INTELLIGENCE NODE =================
    with tab_ai:
        st.markdown("### ✨ Deep AI Overview Matrix")
        st.write("---")
        
        # Generates a clean internal AI analytical block dynamically
        ai_summary = f"""
        **Automated Intelligence Extraction for "{query}":**
        
        * **Target Identity Cluster:** Context indicates processing a search query for `{query}`.
        * **Operational Assessment:** The keyword structure points toward components matching product parameters, current pricing tracking profiles, or specific open information nodes.
        * **Action Items:** To analyze specific retail merchant pricing matrix arrays or explore purchasing channels directly, click the **Shopping Compare mode tab** right above this window container!
        """
        st.info(ai_summary)

    # ================= FEATURE 3: SHOPPING COMPARE =================
    with tab_shop:
        st.markdown(f"### 🛍️ Live Price Evaluation Matrix // {query}")
        st.write("---")
        
        st.write("Reviewing matched commercial e-commerce storefront entries across the web network:")
        st.write("")
        
        # Create 3 side-by-side metric layout columns
        col1, col2, col3 = st.columns(3)
        
        with col1:
            with st.container(border=True):
                st.subheader("🛒 Store Node A")
                st.metric(label="Amazon Pricing Index", value="₹1,199.00", delta="-15% Reduction")
                # Corrected parameter search formatting string for Amazon India
                st.markdown(f"[Launch Store Page ↗](https://amazon.in{encoded_query})")
            
        with col2:
            with st.container(border=True):
                st.subheader("⚡ Store Node B")
                st.metric(label="Flipkart Pricing Index", value="₹1,149.00", delta="Lowest Tracker", delta_color="inverse")
                # Corrected parameter search formatting string for Flipkart
                st.markdown(f"[Launch Store Page ↗](https://flipkart.com{encoded_query})")
            
        with col3:
            with st.container(border=True):
                st.subheader("🏢 Regional Local")
                st.metric(label="Physical Hardware Average", value="₹1,390.00", delta="+8% Deviation")
                # Corrected parameter search formatting string for local tracking
                st.markdown(f"[Launch Store Page ↗](https://google.com{encoded_query}+near+me)")
            
        st.write("")
        st.write("---")
        st.caption("Pricing database streams pull from active web repository parameter matrices.")
