# Enterprise Healthcare Document Intelligence RAG Platform

This repository contains my versioned implementation of a healthcare document intelligence RAG platform.

RAG means Retrieval-Augmented Generation. In simple words, the application will read healthcare PDF documents, store searchable chunks of those documents, retrieve the most relevant chunks for a question, and ask an LLM to answer using only the retrieved evidence.

## Current Status

Current version: Version 15.

Implemented so far:
- GitHub-ready folder structure
- `README.md`
- `PROJECT_NOTES.md`
- `requirements.txt`
- `.env.example`
- `.gitignore`
- production-style backend/frontend split
- production-style folders for backend, frontend, ingestion, RAG, evaluation, data, docs, scripts, and tests
- backend settings loader
- local health check logic
- command-line health check script
- basic unit tests
- PyPDF-based PDF page extraction
- PDF ingestion script for files in `data/raw`
- page-level metadata with file name, file path, page number, and total pages
- LangChain `Document` conversion
- recursive text splitting into chunks
- chunk metadata for future citations and vector storage
- OpenAI embedding client setup
- local ChromaDB vector store setup
- script to build the vector database from PDF chunks
- vector store tests with fake local embeddings
- semantic retrieval from ChromaDB
- search script for retrieving relevant chunks
- retrieval tests with fake local embeddings
- grounded LLM answer generation
- source citations with file name, page number, and chunk ID
- answer-generation tests with a fake local LLM
- FastAPI backend application
- `/health` endpoint
- `/ask` endpoint
- API request and response models
- API tests with mocked RAG pipeline calls
- Streamlit frontend application
- frontend API client for calling FastAPI
- question input, answer display, and citations display
- frontend tests with mocked backend calls
- Unstructured PDF parser path
- Unstructured ingestion script
- parser dependency error handling
- Unstructured parser tests with mocked elements
- OCR fallback for scanned PDFs
- OCR ingestion script
- OCR dependency error handling
- OCR tests with mocked page images
- RAGAS evaluation dataset builder
- sample evaluation examples
- dry-run RAGAS evaluation script
- RAGAS evaluation tests
- Dockerfile for the FastAPI backend
- Dockerfile for the Streamlit frontend
- Docker Compose setup for running backend and frontend together
- Docker ignore rules for secrets, caches, local data, and vector database files
- Docker configuration tests
- AWS S3 configuration settings
- S3 storage helper for listing and uploading healthcare PDFs
- S3 document management script
- S3 storage tests with fake AWS clients
- AWS EC2 deployment path
- EC2 Docker Compose override
- EC2 bootstrap user data script
- EC2 deployment validation script
- EC2 deployment tests

## Tech Stack

- Python
- FastAPI
- Streamlit
- LangChain
- OpenAI API
- ChromaDB
- PyPDF
- Unstructured
- OCR
- RAGAS
- Docker
- AWS S3
- AWS EC2

## Folder Structure

```text
rag-healthcare/
├── backend/
│   ├── Dockerfile       # Container image for the FastAPI backend
│   └── app/
│       ├── __init__.py   # Marks backend app as a Python package
│       ├── api/          # FastAPI routes
│       ├── core/         # Settings and health check logic
│       ├── ingestion/    # PDF parsing and document loading
│       ├── models/       # API request and response schemas
│       ├── rag/          # LangChain documents, chunking, embeddings, retrieval, and answer logic
│       └── storage/      # AWS S3 document storage helpers
├── data/
│   ├── raw/              # Local input PDFs for development
│   ├── processed/        # Future parsed text/chunks
│   └── vector_db/
│       └── chroma/       # Local ChromaDB vector database files
├── deployment/
│   └── ec2/              # AWS EC2 deployment guide and bootstrap script
├── docs/                 # Extra documentation
├── evaluation/           # RAGAS evaluation code
├── frontend/
│   ├── Dockerfile        # Container image for the Streamlit frontend
│   └── app.py            # Streamlit application
├── scripts/              # Helper scripts
├── tests/                # Automated tests
├── .dockerignore         # Files Docker should not copy into images
├── .env.example          # Safe environment variable template
├── .gitignore            # Files Git should ignore
├── docker-compose.ec2.yml # EC2 Compose override
├── docker-compose.yml    # Runs backend and frontend containers together
├── PROJECT_NOTES.md      # Project notes for each version
├── README.md             # Main project overview
└── requirements.txt      # Python dependencies
```

## API Key Safety

Never commit real API keys to GitHub.

This repository includes `.env.example` only. Later, you will create your own local `.env` file on your machine and put real secrets there. The `.env` file is ignored by Git.

## Beginner Setup Notes

Version 2 includes a small runnable Python health check.

Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

Install dependencies when needed:

```bash
pip install -r requirements.txt
```

On Mac, `source .venv/bin/activate` turns on the Python virtual environment for the current terminal.

Run the local health check:

```bash
python3 scripts/health_check.py
```

Run tests:

```bash
python3 -m unittest discover -s tests
```

Run local PDF ingestion:

```bash
python3 scripts/ingest_pdfs.py
```

Run Unstructured PDF ingestion:

```bash
python3 scripts/ingest_unstructured_pdfs.py
```

Unstructured PDF parsing can require extra system dependencies on macOS for some document types. The code reports a clear setup message if optional PDF dependencies are missing.

Run OCR fallback PDF ingestion:

```bash
python3 scripts/ingest_ocr_pdfs.py
```

Real OCR requires Python packages plus system tools. On macOS, this usually means installing Poppler for PDF-to-image conversion and Tesseract for image-to-text OCR.

Run RAGAS evaluation dry run:

```bash
python3 scripts/run_ragas_evaluation.py
```

Run real RAGAS evaluation:

```bash
python3 scripts/run_ragas_evaluation.py --run
```

Real RAGAS evaluation may call an LLM and requires local API keys.

Place local development PDFs in `data/raw/`. This folder is ignored by Git so private or large PDFs do not get uploaded accidentally.

Create LangChain documents and text chunks:

```bash
python3 scripts/chunk_pdfs.py
```

Build the local ChromaDB vector store:

```bash
python3 scripts/build_vector_store.py
```

This command needs a real local `OPENAI_API_KEY` only when there are chunks to embed. Do not paste your key into chat and do not commit `.env`.

Search the local ChromaDB vector store:

```bash
python3 scripts/search_vector_store.py "What does the document say about diabetes?"
```

This command needs real stored vectors and a local `OPENAI_API_KEY`. Tests use fake embeddings and do not call OpenAI.

Generate a grounded answer with citations:

```bash
python3 scripts/answer_question.py "What does the document say about diabetes?"
```

This command needs real stored vectors and a local `OPENAI_API_KEY`. Tests use a fake local LLM and do not call OpenAI.

Run the FastAPI backend:

```bash
python3 scripts/run_api.py
```

Then open:

```text
http://127.0.0.1:8000/health
http://127.0.0.1:8000/docs
```

The `/ask` endpoint needs real stored vectors and a local `OPENAI_API_KEY`.

Run the Streamlit frontend:

```bash
python3 scripts/run_frontend.py
```

Then open:

```text
http://localhost:8501
```

For the full UI workflow, run the FastAPI backend first, then run the Streamlit frontend in a second terminal.

Run the app with Docker:

```bash
docker compose config
docker compose build
docker compose up
```

Then open:

```text
http://127.0.0.1:8000/health
http://localhost:8501
```

Docker Compose passes `.env` into the backend container at runtime if the file exists. The `.env` file is not committed to GitHub and is not copied into Docker images.

The Compose file mounts local `data/` into the backend container so local PDFs and the ChromaDB folder can persist outside the container.

List documents in the configured S3 prefix:

```bash
python3 scripts/s3_documents.py --list
```

Upload local PDFs from `data/raw/` to the configured S3 prefix:

```bash
python3 scripts/s3_documents.py --upload
```

Real S3 commands require AWS credentials configured on your machine and these local `.env` values:

```text
AWS_REGION=us-east-1
AWS_S3_BUCKET_NAME=your_real_bucket_name
AWS_S3_RAW_PREFIX=healthcare-documents/raw
```

Do not paste AWS access keys into chat and do not commit them to GitHub.

Validate the EC2 deployment path:

```bash
python3 scripts/validate_ec2_deployment.py
```

Check the combined local + EC2 Docker Compose configuration:

```bash
docker compose -f docker-compose.yml -f docker-compose.ec2.yml config
```

On an EC2 instance, the prepared start command is:

```bash
docker compose -f docker-compose.yml -f docker-compose.ec2.yml up -d --build
```

The EC2 deployment guide is in `deployment/ec2/README.md`.

## Version Roadmap

- Version 1: Project foundation
- Version 2: Basic Python configuration and health check
- Version 3: Healthcare PDF ingestion with PyPDF
- Version 4: LangChain documents and text splitting
- Version 5: OpenAI embeddings and ChromaDB
- Version 6: Semantic retrieval
- Version 7: Grounded LLM answers with citations
- Version 8: FastAPI backend
- Version 9: Streamlit frontend
- Version 10: Unstructured parsing
- Version 11: OCR fallback for scanned PDFs
- Version 12: RAGAS evaluation
- Version 13: Docker setup
- Version 14: AWS S3 storage path
- Version 15: AWS EC2 deployment path
