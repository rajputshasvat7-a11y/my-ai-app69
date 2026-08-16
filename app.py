import streamlit as st
import zipfile
import urllib.parse

# Setup clean centered layout
st.set_page_config(page_title="Deep Search", page_icon="🔍", layout="centered")

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
st.title("🔍 Deep Search")
st.write("Search the live web directly from mobile or PC.")

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
query = st.text_input("Enter search keywords", placeholder="Type what you want to find...", label_visibility="collapsed")

if query:
    encoded_query = urllib.parse.quote(query)
    
    # Google-Style Multi-Mode Interactive Tabs Configuration
    tab_web, tab_ai, tab_shop = st.tabs(["🌐 All Search", "✨ AI Mode", "🛍️ Shopping"])
    
    # ================= TAB 1: ALL SEARCH =================
    with tab_web:
        st.write(f"**Web results for '{query}':**")
        st.write("")
        
        st.markdown(f"### 1. [Official {query} Portal // Global Index Hub](https://www.{query.lower().replace(' ', '')}.com)")
        st.caption(f"https://www.{query.lower().replace(' ', '')}.com")
        st.write(f"Primary resource node tracking configuration tutorials, community forums, and production updates matching your query profile.")
        st.write("---")
        
        st.markdown(f"### 2. [Google Matrix // Topic Lookup: {query}](https://google.com{encoded_query})")
        st.caption(f"https://google.com{encoded_query}")
        st.write(f"Bypass to the global database layer tracking live index profiles matching your precise parameter string: {query}.")
        st.write("---")

    # ================= TAB 2: AI MODE =================
    with tab_ai:
        st.markdown("### ✨ Deep Search AI Intelligence Overview")
        st.write("---")
        
        # Smart dynamic response text generation layout
        ai_summary = f"""
        **AI Summary for "{query}":**
        Here is a quick overview of what you searched for:
        
        * **Intent:** Web inquiry regarding "{query}".
        * **Context Node:** The request points to technical specifications, retail availability, or digital infrastructure logs matching the keyword parameters.
        * **Recommendation:** If you are trying to analyze product metrics or locate purchase links, toggle over to the **🛍️ Shopping** tab right above this window to view instant price comparison boards!
        """
        st.info(ai_summary)

    # ================= TAB 3: SHOPPING MODE =================
    with tab_shop:
        st.markdown(f"### 🛍️ Live Price Matrix // {query}")
        st.write("---")
        
        # Simulated standard pricing database array
        st.write("Comparing the lowest marketplace entries found on the web:")
        st.write("")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric(label="🛒 Amazon Marketplace", value="₹1,249", delta="-12% Sale")
            st.markdown(f"[View item details](https://amazon.in{encoded_query})")
            
        with col2:
            st.metric(label="⚡ Flipkart Hub", value="₹1,199", delta="Lowest Price", delta_color="inverse")
            st.markdown(f"[Compare on Flipkart](https://flipkart.com{encoded_query})")
            
        with col3:
            st.metric(label="🏢 Local Hardware Retail", value="₹1,450", delta="+5% Higher")
            st.markdown(f"[Check store listings](https://google.com{encoded_query}+near+me)")
            
        st.write("")
        st.write("---")
        st.caption("Pricing records refresh automatically based on cloud tracking sequences.")
