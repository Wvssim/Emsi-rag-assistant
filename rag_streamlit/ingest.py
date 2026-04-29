import os
from typing import List
import shutil

from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

from config import PDF_PATH, CHROMA_DIR, CHUNK_SIZE, CHUNK_OVERLAP, EMBEDDING_MODEL


def _load_pdf(path: str):
    if not os.path.exists(path):
        raise FileNotFoundError(f"PDF not found: {path}")
    loader = PyPDFLoader(path)
    return loader.load()


def _split_docs(docs) -> List:
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
    )
    return splitter.split_documents(docs)


def build_vectorstore(persist: bool = True) -> Chroma:
    docs = _load_pdf(PDF_PATH)
    chunks = _split_docs(docs)

    embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)

    vectordb = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=CHROMA_DIR if persist else None,
    )
    if persist:
        vectordb.persist()
    return vectordb


def load_vectorstore() -> Chroma:
    embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)
    return Chroma(persist_directory=CHROMA_DIR, embedding_function=embeddings)


def ensure_vectorstore() -> Chroma:
    if os.path.isdir(CHROMA_DIR) and os.listdir(CHROMA_DIR):
        return load_vectorstore()
    return build_vectorstore(persist=True)


def rebuild_vectorstore() -> Chroma:
    if os.path.isdir(CHROMA_DIR):
        shutil.rmtree(CHROMA_DIR)
    return build_vectorstore(persist=True)


if __name__ == "__main__":
    build_vectorstore(persist=True)
    print("Chroma index built.")
