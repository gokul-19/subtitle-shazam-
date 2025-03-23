# 🎥🔎 Subtitle Shazam – AI-Powered Subtitle Search Engine

Subtitle Shazam is an AI-powered system designed to enhance search engine relevance for video subtitles. By extracting, processing, and analyzing subtitle data, it efficiently matches relevant video content using embeddings stored in ChromaDB. The system includes subtitle extraction, storage, embedding, and semantic search via a user-friendly Streamlit interface.

---

## 🔥 Features
- ✅ Extract and process subtitle data efficiently
- ✅ Store embeddings with metadata using ChromaDB
- ✅ Perform fast and accurate subtitle matching
- ✅ Build an interactive UI for search and exploration

---

## 🛠️ Technologies Used
- **Python** – Core scripting and data processing
- **Streamlit** – For building the interactive UI
- **ChromaDB** – To store and retrieve subtitle embeddings
- **Google GenAI API** – For generating embeddings and semantic matching
- **Pandas** – For data manipulation and preprocessing

---

## 📽️ Demo Video
🔗 [Watch the Demo on LinkedIn](https://www.linkedin.com/posts/gokul-subtitle-shazam)

---

## 📚 Installation & Usage
```bash
# Clone the repository
git clone https://github.com/Gokul-00/Subtitle-Shazam.git
cd Subtitle-Shazam

# Create a virtual environment
python3 -m venv env

# Activate the virtual environment
# For Linux/Mac
source env/bin/activate
# For Windows
env\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the Streamlit app
streamlit run app.py
```

# 📄 Project Structure
```bash
/subtitle-shazam
├── /app
│   └── app.py
├── /data
│   ├── zipfiles.parquet
│   ├── chroma.sqlite
│   └── subtitle_preprocess.ipynb
├── /notebooks
│   └── subtitle_preprocess.ipynb
├── /db
│   └── subtitle_sem (ChromaDB embeddings)
├── /README.md
└── /requirements.txt
```
# 💡 Future Enhancements
	•	🌐 Add multi-language support for subtitle search
	•	📺 Enable real-time subtitle extraction from videos
	•	🎯 Improve search relevance using advanced semantic models
	•	🚀 Build a recommendation engine for video suggestions

# 🤝 Acknowledgments

A huge thanks to Kanav Bansal Sir and Innomatics Research Labs for their continuous support and mentorship throughout this project! 🙏

# 📬 Contact

Feel free to connect and explore more about this project:

👤 Gokul

📧 Email Me:- gorthigokul77@gmail.com

🔗 LinkedIn:- https://www.linkedin.com/in/gokul-g-a18887270/

# 📢 License

This project is licensed under the MIT License – see the LICENSE file for details.
