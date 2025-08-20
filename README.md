# 📸 Photo Search App

A Streamlit-based Photo Search Application that allows users to search and display photos using an external API. The app includes preprocessing scripts and is easy to deploy locally.

---

## 🚀 Features

* Search for photos by keyword.
* Displays images in a clean Streamlit interface.
* Environment variable support for secure API key management.
* Modular structure with preprocessing scripts.

---

## 📂 Project Structure

```
photo_search/
│── app.py          # Main Streamlit app
│── preprocess.py   # Preprocessing or helper scripts
│── requirements.txt
│── README.md
│── .env            # Your API key (not to be committed)
```

---

## 🛠️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/rahul-1809/photo-search.git
cd photo-search
```

### 2️⃣ Create & Activate Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Add Your API Key

* Create a `.env` file in the root directory.
* Add your API key inside:

```
API_KEY=your_api_key_here
```

### 5️⃣ Run Preprocessing Script

Before launching the app, run any required preprocessing:

```bash
python preprocess.py
```

### 6️⃣ Start the Streamlit App

```bash
streamlit run app.py
```

---

## 📷 Usage

* Open the Streamlit app in your browser.
* Enter a keyword (e.g., mountains, cars, animals).
* View photo results fetched via the API.

---

## 📌 Notes

* Do not commit `.env` file or API keys to GitHub.
* Tested with Python 3.9+.

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

---
