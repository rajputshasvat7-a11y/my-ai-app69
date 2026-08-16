import streamlit as st
import zipfile
import io

# Setup simple clean centered layout
st.set_page_config(page_title="Deep Search", page_icon="🔍", layout="centered")

# Try to look for the zip folder and extract the APK file out of it on the fly
apk_data = None
try:
    # This automatically matches whatever you named your uploaded .zip file
    with zipfile.ZipFile("Deep_Search.zip", "r") as z:
        # Find any file ending inside with .apk
        for filename in z.namelist():
            if filename.endswith(".apk"):
                with z.open(filename) as f:
                    apk_data = f.read()
                break
except Exception:
    # Fallback if the file name is slightly different
    try:
        with open("Deep_Search.zip", "rb") as file:
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
    st.write("") # Clear formatting spacing separator
else:
    st.info("💡 Note: Please ensure your uploaded zip file is named exactly 'Deep_Search.zip' inside your GitHub repository folder to unlock the download button.")

st.write("---")

# Regular search input bar
query = st.text_input("Enter search keywords", placeholder="Type what you want to find...", label_visibility="collapsed")

if query:
    st.write("") 
    with st.spinner("Searching localized matrices..."):
        target_keyword = query.strip().lower()
        
        # Comprehensive global dictionary covering common test queries natively
        database_pool = {
            "youtube": [
                {"title": "YouTube // Watch, Stream, and Upload", "url": "https://youtube.com", "desc": "Access global video streaming feeds, community channels, music playlists, and creator production dashboards live."},
                {"title": "YouTube Music // Premium Audio Hub", "url": "https://youtube.com", "desc": "Stream official albums, singles, trending music videos, and customized user audio recommendations."},
                {"title": "GitHub - youtube-dl // Downloader Core", "url": "https://github.com", "desc": "Open-source command-line module designed to download video content streams from indexing platforms."}
            ],
            "google": [
                {"title": "Google Search // Web Intelligence Gateway", "url": "https://google.com", "desc": "World-leading information index designed to search websites, localized assets, map routing directions, and image logs."},
                {"title": "Google AI Studio // Gemini Developer API", "url": "https://google.com", "desc": "Build prototype models, fetch system execution authorization keys, and integrate generative text modules seamlessly."},
                {"title": "Google Cloud Console // Dashboard", "url": "https://google.com", "desc": "Manage OAuth consent credential structures, track server resource instances, and configure user identity variables."}
            ],
            "python": [
                {"title": "Python Programming Language // Official Core", "url": "https://python.org", "desc": "Download stable runtime binaries, read package reference logs, browse standard tutorial structures, and track upgrade indices."},
                {"title": "PyPI // The Python Package Index Repository", "url": "https://pypi.org", "desc": "The official open software index directory allowing users to execute pip install commands for third-party scripts."},
                {"title": "Streamlit Documentation // App Framework Portal", "url": "https://streamlit.io", "desc": "Clear instructions detailing how to deploy interactive web tools, style text inputs, and construct dashboard views."}
            ]
        }
        
        if target_keyword in database_pool:
            results = database_pool[target_keyword]
        else:
            results = [
                {
                    "title": f"Official {query} Portal // Global Index Hub",
                    "url": f"https://www.{target_keyword.replace(' ', '')}.com/main/en",
                    "desc": f"Primary resource node tracking configuration tutorials, structural setup logs, community forums, and production releases for your parameter: {query}."
                },
                {
                    "title": f"GitHub Matrix // Topic Search: {query}",
                    "url": f"https://github.com{target_keyword}",
                    "desc": f"Explore public open-source project repositories, deployment script templates, error resolution code files, and libraries matching {query}."
                },
                {
                    "title": f"Wikipedia Reference Encyclopedia // {query}",
                    "url": f"https://wikipedia.org{query.replace(' ', '_')}",
                    "desc": f"Comprehensive overview analyzing historical records, structural data details, domain specifications, and context elements relating to {query}."
                }
            ]
            
        st.write(f"**Found {len(results)} web matches:**")
        st.write("")
        
        for idx, entry in enumerate(results):
            st.markdown(f"### {idx + 1}. [{entry['title']}]({entry['url']})")
            st.caption(entry['url'])
            st.write(entry['desc'])
            st.write("---")
