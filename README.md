# Enterprise Healthcare Document Intelligence RAG Platform

I built this project as a production-style healthcare document intelligence RAG platform.

My goal was to rebuild the project from scratch and understand each part of a real GenAI/RAG system: PDF ingestion, parsing, chunking, embeddings, vector search, grounded answer generation, citations, API development, frontend development, evaluation, Docker, and AWS deployment planning.

RAG means Retrieval-Augmented Generation. In simple words, my application reads healthcare PDF documents, breaks them into searchable chunks, stores those chunks in a vector database, retrieves the most relevant chunks for a user question, and generates an answer using the retrieved evidence.

## Current Status

Current version: Version 15.

At this stage, I have implemented the full resume-aligned project path:

- healthcare PDF ingestion with PyPDF
- Unstructured parsing path for more complex PDFs
- OCR fallback path for scanned PDFs
- LangChain `Document` objects
- LangChain recursive text splitting
- OpenAI embedding client setup
- ChromaDB local vector database setup
- semantic retrieval from ChromaDB
- grounded LLM answer generation
- source citations with file name, page number, and chunk ID
- FastAPI backend with `/health` and `/ask` endpoints
- Streamlit frontend for asking questions and viewing citations
- RAGAS evaluation support
- Docker setup for backend and frontend
- AWS S3 document storage path
- AWS EC2 deployment path
- automated tests for the main project layers

## Tech Stack

- Python
- FastAPI
- Streamlit
- LangChain
- OpenAI API
- ChromaDB
- PyPDF
- Unstructured
- OCR with `pdf2image` and `pytesseract`
- RAGAS
- Docker
- AWS S3
- AWS EC2

## What I Built

I organized the project like a production-style application instead of keeping everything in one script.

The backend contains the ingestion, RAG, API, storage, and configuration code. The frontend contains the Streamlit UI. Scripts are used for local workflows like ingestion, vector store building, question answering, evaluation, S3 document actions, and EC2 deployment validation. Tests cover the important behavior without requiring real API keys or real AWS calls.

## Folder Structure

```text
rag-healthcare/
├── backend/
│   ├── Dockerfile
│   └── app/
│       ├── api/          # FastAPI routes
│       ├── core/         # Settings and health check logic
│       ├── ingestion/    # PyPDF, Unstructured, and OCR parsing
│       ├── models/       # API request and response schemas
│       ├── rag/          # Chunking, embeddings, vector store, retrieval, answers
│       └── storage/      # AWS S3 document storage helpers
├── data/
│   ├── raw/              # Local input PDFs for development
│   ├── processed/        # Parsed/processed outputs
│   └── vector_db/
│       └── chroma/       # Local ChromaDB files
├── deployment/
│   └── ec2/              # AWS EC2 deployment guide and bootstrap script
├── evaluation/           # RAGAS evaluation code
├── frontend/             # Streamlit frontend
├── scripts/              # Local helper scripts
├── tests/                # Automated tests
├── .dockerignore
├── .env.example
├── .gitignore
├── docker-compose.ec2.yml
├── docker-compose.yml
├── PROJECT_NOTES.md
├── README.md
└── requirements.txt
```

## How The RAG Pipeline Works

The project pipeline is:

```text
Healthcare PDFs
-> PDF parsing with PyPDF, Unstructured, or OCR
-> LangChain Document objects
-> text chunks
-> OpenAI embeddings
-> ChromaDB vector storage
-> semantic retrieval
-> grounded LLM answer generation
-> citations
-> FastAPI backend
-> Streamlit frontend
```

For local development, PDFs can be placed in `data/raw/`.

For the cloud storage path, I added AWS S3 helper code for listing and uploading source PDFs.

For the deployment path, I added Docker and an AWS EC2 deployment guide.

## API Key And Secret Safety

I do not commit real API keys or cloud credentials.

This repository includes `.env.example` only. A real local `.env` file should be created on the developer machine and should never be committed to GitHub.

Example local values:

```text
OPENAI_API_KEY=your_real_key_here
AWS_REGION=us-east-1
AWS_S3_BUCKET_NAME=your_real_bucket_name
AWS_S3_RAW_PREFIX=healthcare-documents/raw
```

The `.env` file is ignored by Git.

## Local Setup

Create and activate a Python virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the health check:

```bash
python3 scripts/health_check.py
```

Run tests:

```bash
python3 -m unittest discover -s tests
```

## Common Local Workflows

Parse local PDFs with PyPDF:

```bash
python3 scripts/ingest_pdfs.py
```

Parse PDFs with Unstructured:

```bash
python3 scripts/ingest_unstructured_pdfs.py
```

Run OCR fallback for scanned PDFs:

```bash
python3 scripts/ingest_ocr_pdfs.py
```

Create chunks:

```bash
python3 scripts/chunk_pdfs.py
```

Build the ChromaDB vector store:

```bash
python3 scripts/build_vector_store.py
```

Ask a question from the command line:

```bash
python3 scripts/answer_question.py "What does the document say about diabetes?"
```

Run RAGAS evaluation dry run:

```bash
python3 scripts/run_ragas_evaluation.py
```

## Running The App

Run the FastAPI backend:

```bash
python3 scripts/run_api.py
```

Open:

```text
http://127.0.0.1:8000/health
http://127.0.0.1:8000/docs
```

Run the Streamlit frontend:

```bash
python3 scripts/run_frontend.py
```

Open:

```text
http://localhost:8501
```

For the full local UI workflow, I run FastAPI in one terminal and Streamlit in another terminal.

## Docker

Build and run the app with Docker Compose:

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

## AWS S3 Path

List documents in the configured S3 prefix:

```bash
python3 scripts/s3_documents.py --list
```

Upload local PDFs from `data/raw/` to S3:

```bash
python3 scripts/s3_documents.py --upload
```

Real S3 commands require AWS credentials configured locally. I do not store AWS access keys in this repository.

## AWS EC2 Path

Validate the EC2 deployment files:

```bash
python3 scripts/validate_ec2_deployment.py
```

Check the combined local and EC2 Docker Compose configuration:

```bash
docker compose -f docker-compose.yml -f docker-compose.ec2.yml config
```

On an EC2 instance, the prepared start command is:

```bash
docker compose -f docker-compose.yml -f docker-compose.ec2.yml up -d --build
```

The EC2 deployment guide is in `deployment/ec2/README.md`.

## Testing Approach

I wrote tests so I can verify the project safely without calling paid or external services every time.

The tests use fake embeddings, fake LLM behavior, mocked parser behavior, and fake AWS clients where needed. Real OpenAI and AWS calls are only needed when running the actual local pipeline with real credentials.


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
