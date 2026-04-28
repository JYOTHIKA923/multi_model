# multi_model  
# 🔍 AI Image Search System

An AI-powered product search web application that allows users to upload an image and instantly find visually similar products using **CLIP embeddings** and **ChromaDB vector database**.

Designed with a premium modern UI and built using **Flask + Python + AI models**.

---

# 🚀 Features

## 👤 User Features
- Upload any product image
- Find top similar products instantly
- Similarity score (%) display
- Product match labels:
  - Exact Match
  - Same Product Variant
  - Similar Product
  - Related Product
- Search history tracking
- Like / Dislike feedback system
- Light / Dark mode UI
- Responsive premium dashboard

---

## 🔐 Admin Features
- Secure admin panel
- Add new products with image upload
- Delete products by ID
- Real-time inventory update
- Product embeddings auto-generated

---

# 🧠 AI Technology Used

## CLIP Model
Used for converting product images into smart feature vectors (embeddings).

## ChromaDB
Stores embeddings and performs ultra-fast similarity search.

---

# 🏗️ Tech Stack

- Python
- Flask
- HTML
- CSS
- JavaScript
- ChromaDB
- Torch
- Transformers
- Pillow
- NumPy

---

# 📂 Project Structure

```bash
AI-Image-Search/
│── app.py
│── db.py
│── embed.py
│── requirements.txt
│── history.txt
│── feedback.txt
│
├── templates/
│   └── index.html
│
├── static/
│   ├── style.css
│   ├── script.js
│   ├── uploads/
│   └── images/

# ⚙️ Installation
1️⃣ Clone Repository
git clone https://github.com/yourusername/AI-Image-Search.git
cd AI-Image-Search

# 2️⃣ Install Requirements
pip install -r requirements.txt

# 3️⃣ Run Project
python app.py

# 🌐 Open In Browser
http://127.0.0.1:5000

# 📸 How It Works
- User uploads image
- CLIP extracts image embedding
- ChromaDB compares vectors
- Similar products retrieved
- Results ranked by similarity score

# 📈 Future Improvements
- Barcode scanner
- Voice search
- Multi-image search
- Product recommendation engine
- Login authentication
- Cloud deployment


