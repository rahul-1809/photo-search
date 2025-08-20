import os
import pickle
import numpy as np
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai
from PIL import Image

# Load API key
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Load preprocessed index
with open("photo_index.pkl", "rb") as f:
    photo_index = pickle.load(f)

# Get embedding for query
def get_embedding(text):
    emb = genai.embed_content(model="models/embedding-001", content=text)
    return emb["embedding"]

# Cosine similarity
def cosine_similarity(a, b):
    a, b = np.array(a), np.array(b)
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

# Search photos
def search_photos(query, top_k=5):
    query_emb = get_embedding(query)
    scored = [
        (item, cosine_similarity(query_emb, item["embedding"])) 
        for item in photo_index
    ]
    scored.sort(key=lambda x: x[1], reverse=True)
    return [x[0] for x in scored[:top_k]]

# Streamlit UI
st.title("📷 Smart Photo Search (with Gemini)")

query = st.text_input("Search your photos (e.g., 'dog running on grass')")

if query:
    results = search_photos(query)
    st.subheader("🔎 Search Results:")
    for r in results:
        st.image(r["file"], caption=r["caption"])
