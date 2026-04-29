import streamlit as st

from rag import get_qa_chain, format_sources
from ingest import rebuild_vectorstore
from config import PDF_PATH, CHROMA_DIR, GROQ_MODEL

st.set_page_config(page_title="EMSI Chatbot RAG", page_icon="🎓")

st.title("🎓 EMSI Chatbot (RAG)")
st.caption("Base de connaissances: Brochure-EMSI.pdf")

with st.sidebar:
    st.subheader("Configuration")
    st.write(f"PDF: `{PDF_PATH}`")
    st.write(f"Index: `{CHROMA_DIR}`")
    st.write(f"Modèle: `{GROQ_MODEL}`")
    rebuild = st.button("Reconstruire l'index")

if rebuild:
    rebuild_vectorstore()
    st.success("Index prêt.")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

prompt = st.chat_input("Posez une question sur l'EMSI")

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        answer = ""
        try:
            qa = get_qa_chain()
            result = qa(prompt)
            answer = result.get("result", "")
            st.markdown(answer)

            sources = format_sources(result.get("source_documents", []))
            if sources:
                st.markdown("**Sources**")
                for src in sources:
                    st.markdown(f"- {src['source']} (page {src['page']})")
        except Exception as exc:
            st.error(str(exc))

    if answer:
        st.session_state.messages.append({"role": "assistant", "content": answer})
