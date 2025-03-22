import streamlit as st
import chromadb
import time

# Load the dataset
path = "db"
client = chromadb.PersistentClient(path=path)
client.heartbeat()
collection = client.get_collection(name="subtitle_sem")

# Define the search function
def similar_title(query_text, language, year):
    filters = {}
    if language != "Any":
        filters["subtitle_language"] = language
    if year:
        filters["release_year"] = year

    result = collection.query(
        query_texts=query_text,
        include=["metadatas", "distances"],
        n_results=5
    )
    ids = result['ids'][0]
    distances = result['distances'][0]
    metadatas = result['metadatas'][0]
    
    # Apply filters if language or year is selected
    filtered_results = []
    for i, metadata in enumerate(metadatas):
        if (
            (language == "Any" or metadata.get('subtitle_language') == language)
            and (not year or int(metadata.get('release_year', 0)) == year)
        ):
            filtered_results.append((ids[i], distances[i], metadata))
    
    # Sort by distance (lower = better match)
    sorted_data = sorted(filtered_results, key=lambda x: x[1])  
    return sorted_data

# App UI
st.title('🎥 Subtitle Sleuth: Discover Hidden Gems! 🔍')
st.markdown("""
    **Tired of skipping through trailers?**  
    🔎 Search by **subtitle snippets** and jump straight into the action! 🎬  
    Whether you're looking for **classic quotes** or **iconic dialogues**, we've got you covered! 🚀
""")

# User input for search
query_text = st.text_input('💡 Enter a phrase or keyword from the subtitle:')
language = st.selectbox(
    '🌐 Choose Subtitle Language:',
    ['Any', 'English', 'Spanish', 'French', 'German', 'Italian']
)
year = st.slider('📅 Year of Release:', 2000, 2025, 2020)
search = st.button("🔎 Find Subtitles")

# Tips for better search
st.markdown("""
    💡 **Pro Tip:** Try searching for exact phrases or memorable dialogues for better results!
""")

# Search logic
if search:
    if not query_text:
        st.warning("⚠️ Please enter a search query!")
    else:
        with st.spinner('🔍 Searching for the best matches...⏳'):
            time.sleep(2)  # Optional delay for better UX
            result = similar_title(query_text, language, year)

        # Display results
        if result:
            st.success('✅ Here are the most relevant subtitle results:')
            for subtitle_id, distance, metadata in result:
                subtitle_name = metadata['subtitle_name']
                subtitle_link = f"https://www.opensubtitles.org/en/subtitles/{subtitle_id}"
                subtitle_lang = metadata.get('subtitle_language', 'Unknown')
                release_year = metadata.get('release_year', 'Unknown')
                st.markdown(
                    f"🎞️ [{subtitle_name}]({subtitle_link})  \n"
                    f"🌐 Language: **{subtitle_lang}** | 📅 Year: **{release_year}**  \n"
                    f"⚡ Relevance Score: **{round(distance, 2)}**"
                )
        else:
            st.warning("⚠️ No relevant subtitles found. Try a different query!")