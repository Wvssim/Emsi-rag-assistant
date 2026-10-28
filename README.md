# EMSI Assistant

This repository contains two related components:

- An Android application in `app/`.
- A document-question-answering prototype in `rag_streamlit/`, implemented with retrieval-augmented generation (RAG).

The Streamlit assistant answers questions using the EMSI brochure as its knowledge source.

## RAG pipeline

1. Load and split `Brochure-EMSI.pdf` into text chunks.
2. Generate embeddings with Sentence Transformers.
3. Persist and search the vector index with ChromaDB.
4. Retrieve relevant passages and send the context to a Groq-hosted language model.
5. Present the response in a Streamlit chat interface.

LangChain coordinates the retrieval and generation steps; PyPDF is used to read the PDF.

## Run the Streamlit application

Requirements: Python 3.10+, a Groq API key, and `Brochure-EMSI.pdf` at the repository root.

From `rag_streamlit/`:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
Copy-Item .env.example .env
```

Add the key to `.env`:

```ini
GROQ_API_KEY=your_key_here
```

Build or refresh the local vector index, then launch the interface:

```powershell
python ingest.py
streamlit run app.py
```

The index is generated locally from the brochure. Keep API keys in the local environment file and never commit them.

## Repository layout

```text
app/                 Android application
Brochure-EMSI.pdf    source document for the RAG assistant
rag_streamlit/
  app.py             Streamlit interface
  ingest.py          document ingestion and indexing
  rag.py             retrieval and generation
  config.py          paths and model configuration
  requirements.txt   Python dependencies
```

For component-specific instructions, see `rag_streamlit/README.md`.
