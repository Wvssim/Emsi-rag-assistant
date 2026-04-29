import os

from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY", "").strip()
GROQ_MODEL = os.getenv("GROQ_MODEL", "llama-3.1-8b-instant").strip()
PDF_PATH = os.getenv("PDF_PATH", "../Brochure-EMSI.pdf").strip()
CHROMA_DIR = os.getenv("CHROMA_DIR", "chroma_db").strip()

CHUNK_SIZE = 1000
CHUNK_OVERLAP = 150
TOP_K = 4

EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

