# ragpdfchatbot


The application enables uploading of a PDF file along with asking questions about it. The application employs ChromaDB as vector store, Sentence Transformers for embedding generation and Google's Gemini for generating context-aware responses.

---

## 🚀 Features

- Upload any PDF document
- Extract text from the PDF automatically
- Split the text into chunks
- Generate embeddings using Sentence Transformers
- Store embeddings in ChromaDB
- Retrieve the most relevant document chunks
- Answer questions using Google Gemini
- Interactive Gradio interface

---

## 🛠️ Technologies Used

- Python
- Gradio
- Google Gemini API
- ChromaDB
- Sentence Transformers
- PyPDF
- python-dotenv

---

## 📂 Project Structure

```
PDF-RAG-Chatbot/
│── app.py
│── requirements.txt
│── .env
│── .gitignore
│── README.md
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/PDF-RAG-Chatbot.git

cd PDF-RAG-Chatbot
```

### 2. Create a virtual environment (Optional)

```bash
python -m venv venv
```

Activate it:

**Windows**

```bash
venv\Scripts\activate
```

**Linux/Mac**

```bash
source venv/bin/activate
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Create a `.env` file

Create a file named `.env` in the project directory.

```env
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
```

---

###
