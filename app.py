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
            # Bulletproof connection to the official Wikipedia search matrix
            encoded_query = urllib.parse.quote(query)
            api_url = f"https://wikipedia.org{encoded_query}&limit=8&namespace=0&format=json"
            
            req = urllib.request.Request(
                api_url, 
                headers={'User-Agent': 'DeepSearchEngine/1.0 (Contact: admin@example.com)'}
            )
            
            with urllib.request.urlopen(req) as response:
                data = json.loads(response.read().decode('utf-8'))
                
                # Wikipedia open search format returns: [query, [titles], [descriptions], [links]]
                titles = data[1]
                snippets = data[2]
                links = data[3]

            min_length = len(links)

            if min_length > 0:
                st.write(f"**Found {min_length} web matches:**")
                st.write("")
                
                for idx in range(min_length):
                    title_text = titles[idx]
                    desc_text = snippets[idx] if snippets[idx] else "Click link to view full entry."
                    raw_url = links[idx]
                    
                    # Displaying in clean normal markdown text
                    st.markdown(f"### {idx + 1}. [{title_text}]({raw_url})")
                    st.caption(raw_url)
                    st.write(desc_text)
                    st.write("---")
            else:
                st.info("No search matches found. Try different keywords.")

        except Exception as e:
            st.error(f"Network error. Please try hitting enter again. (Details: {e})")
