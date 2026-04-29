from typing import Dict, List

from langchain_groq import ChatGroq
from langchain.chains import RetrievalQA

from config import GROQ_API_KEY, GROQ_MODEL, TOP_K
from ingest import ensure_vectorstore


def get_qa_chain():
    if not GROQ_API_KEY:
        raise ValueError("GROQ_API_KEY is missing. Set it in .env.")

    vectordb = ensure_vectorstore()

    llm = ChatGroq(
        groq_api_key=GROQ_API_KEY,
        model_name=GROQ_MODEL,
        temperature=0.2,
    )

    retriever = vectordb.as_retriever(search_kwargs={"k": TOP_K})

    return RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever,
        return_source_documents=True,
    )


def format_sources(source_docs: List) -> List[Dict[str, str]]:
    sources = []
    for doc in source_docs:
        src = doc.metadata.get("source", "PDF")
        page = doc.metadata.get("page", "?")
        sources.append({"source": src, "page": str(page)})
    return sources

