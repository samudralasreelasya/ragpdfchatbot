import uuid
import chromadb
import google.generativeai as genai
import gradio as gr
from pypdf import PdfReader
from sentence_transformers import SentenceTransformer

# API Configuration
load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY not found in .env file")

genai.configure(api_key=GEMINI_API_KEY)
llm = genai.GenerativeModel("gemini-2.5-flash")

# Load embedding model
print("Loading embedding model...")
embedder = SentenceTransformer("all-MiniLM-L6-v2")
print("Embedding model loaded!")

# Initialize ChromaDB client
client = chromadb.Client()
collection = client.get_or_create_collection("rag_docs")


def extract_text(pdf):
    reader = PdfReader(pdf.name)
    text = ""
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"
    return text


def chunk_text(text, size=300):
    return [text[i : i + size] for i in range(0, len(text), size)]


def upload_pdf(pdf):
    global collection
    if pdf is None:
        return "Please upload a valid PDF file."

    text = extract_text(pdf)
    chunks = chunk_text(text)
    print(f"Chunks Created: {len(chunks)}")

    embeddings = embedder.encode(chunks).tolist()

    # Safely clear old data
    try:
        client.delete_collection("rag_docs")
    except Exception:
        pass

    collection = client.get_or_create_collection("rag_docs")
    collection.add(
        documents=chunks,
        embeddings=embeddings,
        ids=[str(uuid.uuid4()) for _ in chunks],
    )
    return f"PDF Indexed Successfully ({len(chunks)} chunks)"


def ask(question):
    query_embedding = embedder.encode(question).tolist()
    result = collection.query(query_embeddings=[query_embedding], n_results=3)

    # Combine and slice to avoid breaking LLM context windows
    context = "\n".join(result["documents"][0])
    context = context[:4000]

    prompt = f"""
    Answer the question ONLY using the context below.
    If you cannot find the answer in the document, reply exactly with: "I couldn't find the answer in the document."

    Context:
    {context}

    Question: {question}
    """
    response = llm.generate_content(prompt)
    return response.text
