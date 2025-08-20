import os
import pickle
from PIL import Image
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

photos_dir = "photos"
output_file = "photo_index.pkl"

# Get caption using Gemini
def get_caption(image_path):
    img = Image.open(image_path)
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(["Describe this image in one sentence.", img])
    return response.text.strip()

# Get embedding using Gemini
def get_embedding(text):
    emb = genai.embed_content(model="models/embedding-001", content=text)
    return emb["embedding"]

def preprocess_images():
    index = []
    for file in os.listdir(photos_dir):
        path = os.path.join(photos_dir, file)
        if os.path.isfile(path):
            try:
                caption = get_caption(path)
                embedding = get_embedding(caption)
                index.append({"file": path, "caption": caption, "embedding": embedding})
                print(f"Processed: {file} → {caption}")
            except Exception as e:
                print(f"Error with {file}: {e}")

    with open(output_file, "wb") as f:
        pickle.dump(index, f)
    print(f"✅ Index saved to {output_file}")

if __name__ == "__main__":
    preprocess_images()
