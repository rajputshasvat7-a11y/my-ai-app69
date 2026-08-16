import streamlit as st
import urllib.request
import urllib.parse
import json

# Setup simple clean centered layout
st.set_page_config(page_title="Deep Search", page_icon="🔍", layout="centered")

# Normal standard headers
st.title("🔍 Deep Search")
st.write("Search the live web directly from mobile or PC.")
st.write("---")

# Regular search input bar
query = st.text_input("Enter search keywords", placeholder="Type what you want to find...", label_visibility="collapsed")

if query:
    st.write("") 
    with st.spinner("Searching..."):
        try:
            # High-speed decentralized network processing layer
            encoded_query = urllib.parse.quote(query)
            api_url = f"https://searx.be{encoded_query}&format=json"
            
            req = urllib.request.Request(
                api_url, 
                headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
            )
            
            with urllib.request.urlopen(req) as response:
                data = json.loads(response.read().decode('utf-8'))
                results = data.get('results', [])

            # Extract top 8 results
            min_length = min(len(results), 8)

            if min_length > 0:
                st.write(f"**Found {min_length} web matches:**")
                st.write("")
                
                for idx in range(min_length):
                    result = results[idx]
                    raw_url = result.get('url', '')
                    title_text = result.get('title', 'Untitled Entry')
                    desc_text = result.get('content', 'No content details available.')
                    
                    # Displaying in clean normal markdown text
                    st.markdown(f"### {idx + 1}. [{title_text}]({raw_url})")
                    st.caption(raw_url)
                    st.write(desc_text)
                    st.write("---")
            else:
                st.info("No search matches found. Try different keywords.")

        except Exception as e:
            st.error(f"Network timeout. Please hit enter to try again. (Details: {e})")
