# EMSI Chatbot RAG (Streamlit)

## Prerequis
- Python 3.10+
- Une cle API Groq
- Le fichier `Brochure-EMSI.pdf`

## Installation
1. Créer un environnement virtuel (optionnel mais recommande).
2. Installer les dependances.

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Configuration
- Copier `.env.example` vers `.env` et renseigner la cle Groq.
- Placer le PDF dans la racine du repo (`../Brochure-EMSI.pdf` depuis `rag_streamlit/`) ou changer `PDF_PATH`.

## Lancer l'indexation
```powershell
python ingest.py
```

## Lancer l'application
```powershell
streamlit run app.py
```

## Test rapide
```powershell
python run_local.py
```

## Notes
- L'index Chroma est stocke dans `chroma_db/`.
- Le premier lancement peut etre plus long (telechargement des embeddings).

