# 🩺 Medibot, A Medical Chatbot
A Retrieval-Augmented Generation (RAG) chatbot built with LangChain, OpenAI, Pinecone, and Flask, designed to answer questions with reference to the GALE Encyclopedia of Medicine (Third Edition).

⚠️ Disclaimer: This chatbot is intended for informational purposes only. It does not provide medical advice, diagnosis, or treatment.

![image](https://github.com/user-attachments/assets/701bbc62-4ad0-40a1-b6fd-333440152844)

## Features
- RAG (Retrieval-Augmented Generation) Pipeline
- Combines OpenAI LLM with retrieval from The GALE encyclopedia of medicine for accurate responses
- Web interface

## Tech Stack

| Component      | Technology             |
|----------------|------------------------|
| Language Model | OpenAI GPT |
| Retrieval DB   | Pinecone (Vector DB)   |
| Framework      | LangChain              |
| Backend/API    | Flask                  |
| Embeddings     | OpenAI Embeddings |
| Chunking       | LangChain Text Splitters |

## 🔧 Setup Guide

### 1. Clone the Repository

### 2. Create a Conda environment
Note: Anaconda installation required
```bash
conda create -n medibot python=3.10 -y
conda activate medibot
```

### 3. Install Dependencies
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Configure Environment
You will need an OpenAI API key (payment required) and Pinecone API Key (free). Create a .env file in the root with the following:
```env
OPENAI_API_KEY=your-openai-api-key
PINECONE_API_KEY=your-pinecone-api-key
```

### 6. 🧠 Generate Vector Index
Run the script to load and index the documents into Pinecone:
```python
python store_index.py
```
Note: **This will take several minutes** You only need to run this once during installation, **or** if you modify the reference Data.

### 7. Run the Flask app
```bash
flask run
```
If the app doesn't start automatically, paste http://localhost:5000/ into your browser.

