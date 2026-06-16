# Project Notes

## Project Name

Enterprise Healthcare Document Intelligence RAG Platform

## Project Overview

This project is my implementation of an enterprise-style healthcare document intelligence RAG platform. I am building it in clear versions so each layer is understandable, testable, and easy to explain.

Target stack:

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

Each version adds one focused layer instead of trying to build the full system at once.

## Version 1: Project Foundation

### 1. What I Built

I created the clean starting structure for the project.

Version 1 includes:
- A main `README.md`
- A project journal called `PROJECT_NOTES.md`
- A `requirements.txt` file listing planned Python dependencies
- A safe `.env.example` file with placeholder environment variables
- A `.gitignore` file to prevent secrets, virtual environments, caches, and local data from being committed
- Empty folders for backend code, frontend code, ingestion code, RAG code, evaluation code, scripts, tests, documents, and data
- A production-style split between `backend/` and `frontend/`

### 2. Why I Built It

Production projects need organization before code.

If everything is placed in one random file, the project becomes hard to understand, hard to test, hard to deploy, and hard to explain in interviews.

This foundation gives every future part of the RAG system a clear home.

### 3. What Each File And Folder Does

`README.md`

This is the first file people usually read on GitHub. It explains the project purpose, current version, folder structure, planned stack, and safety rules.

`PROJECT_NOTES.md`

This is the project journal. It explains what I built in each version, why it matters, and how it connects to the final RAG system.

`requirements.txt`

This lists Python packages that the project will use over time. In Version 1, it is a planned dependency list. Later versions will start using these packages in code.

`.env.example`

This shows which environment variables the project expects, but it does not contain real secrets.

`.gitignore`

This tells Git which files and folders should not be uploaded to GitHub. Most importantly, it ignores `.env`, where real API keys will live later.

`backend/`

This will contain the backend service. In this project, the backend will eventually be a FastAPI application.

`backend/app/`

This is the main Python application package for the backend.

`backend/app/__init__.py`

This marks `backend/app/` as a Python package. In simple words, it helps Python import code from this folder cleanly.

`backend/app/api/`

This will contain FastAPI routes in a later version. A route is an HTTP endpoint, such as `/health` or `/ask`.

`backend/app/core/`

This will contain shared settings and configuration, such as loading environment variables.

`backend/app/ingestion/`

This will contain PDF loading and parsing code, including PyPDF, Unstructured, and OCR fallback in future versions.

`backend/app/rag/`

This will contain the RAG pipeline: chunking, embeddings, vector search, retrieval, and answer generation.

`backend/app/models/`

This will contain request and response schemas later. Schemas define the shape of data coming into and going out of the API.

`frontend/`

This will contain the Streamlit user interface later.

`evaluation/`

This will contain RAGAS evaluation code later.

`data/raw/`

This is where local healthcare PDF files can be placed during development.

`data/processed/`

This will store processed intermediate data later, such as extracted text or chunks.

`data/vector_db/`

This will contain local vector database files during development.

`data/vector_db/chroma/`

This will store the local ChromaDB vector database later. ChromaDB is where the future embeddings will be saved so the system can do semantic search.

`docs/`

This will hold extra project documentation.

`scripts/`

This will hold helper scripts, such as ingestion or evaluation commands.

`tests/`

This will hold automated tests later.

### 4. How The Code Works In Simple Words

Version 1 does not contain runnable application code yet.

Instead, it creates the project map.

Think of it like building shelves before filling them:
- PDF ingestion code will go in `backend/app/ingestion/`
- RAG logic will go in `backend/app/rag/`
- API code will go in `backend/app/api/`
- UI code will go in `frontend/`
- evaluation code will go in `evaluation/`

### 5. How This Step Connects To The Full RAG Pipeline

The final RAG pipeline will look like this:

```text
Healthcare PDFs
→ PDF parsing
→ OCR fallback if scanned
→ LangChain documents
→ Text chunks
→ OpenAI embeddings
→ ChromaDB vector store
→ Semantic retrieval
→ Grounded LLM answer
→ Source citations
→ FastAPI backend
→ Streamlit frontend
→ RAGAS evaluation
→ Docker and AWS deployment
```

Version 1 prepares folders for every stage of that pipeline.

### 6. How This Step Connects To The Resume

This version creates the professional foundation for the project.

A clear way to describe this version is:

"I established a production-style project structure with separate backend, frontend, data, evaluation, documentation, and test areas for a healthcare RAG platform."

### 7. What Changed From The Previous Version

There was no previous version.

Version 1 is the starting point.

### 8. What Output You Should Expect

You should see a clean project folder with:
- `README.md`
- `PROJECT_NOTES.md`
- `requirements.txt`
- `.env.example`
- `.gitignore`
- project folders for future code
- a clear `backend/app/` structure for future FastAPI code
- a separate `frontend/` folder for future Streamlit code

No web app runs yet.
No backend API runs yet.
No PDFs are processed yet.
No embeddings are created yet.

### 9. Common Mistakes And How To Fix Them

Mistake: Putting a real OpenAI API key in GitHub.

Fix: Put real keys only in `.env`, never in `.env.example`, and make sure `.env` is listed in `.gitignore`.

Mistake: Expecting the app to run in Version 1.

Fix: Version 1 is only the foundation. Running code starts in a later version.

Mistake: Installing every dependency before understanding the project.

Fix: Install and use dependencies gradually as each version needs them.

Mistake: Uploading local data files to GitHub.

Fix: Keep local PDFs and vector database files ignored unless a specific sample file is safe to publish.

### 10. What I Will Build Next

In Version 2, I will add a tiny working Python foundation:
- basic settings loader
- simple project health check
- possibly a small command that proves the environment is working

The full RAG system should still be added gradually, one layer at a time.

## Version 1 Interview Preparation

### Most Likely Interview Questions

Question: What did you build in Version 1?

Short answer: I created the GitHub-ready foundation for a healthcare RAG platform.

Detailed answer: I set up the project structure, documentation, dependency list, environment variable template, and Git ignore rules. I separated future backend, frontend, ingestion, RAG, evaluation, data, scripts, and tests into clear folders so the system can grow in a clean way.

Follow-up: Why not start directly with embeddings and retrieval?

Answer: Because production projects need structure first. A clean foundation makes the code easier to test, explain, deploy, and maintain.

What not to say: "I built the whole RAG app in Version 1."

Red flag to avoid: Claiming features that are only planned.

### Theory Questions

Question: What is RAG?

Short answer: RAG means Retrieval-Augmented Generation.

Detailed answer: RAG is a pattern where we retrieve relevant information from documents first, then give that information to an LLM so it can answer with better grounding. Instead of relying only on the model's memory, the system uses external documents as evidence.

Follow-up: Why is RAG useful in healthcare?

Answer: Healthcare documents can be long and detailed. RAG helps answer questions using specific source documents and citations, which is better than asking the LLM to guess.

What not to say: "RAG guarantees perfect answers."

Red flag to avoid: Ignoring hallucination risk.

### Coding Questions

Question: Why did you create separate folders?

Short answer: To separate responsibilities.

Detailed answer: API code, ingestion code, RAG logic, frontend code, and evaluation code do different jobs. Keeping them separate makes the project easier to understand and modify.

Follow-up: Where would PDF parsing code go?

Answer: In `backend/app/ingestion/`.

Follow-up: Where would vector search code go?

Answer: In `backend/app/rag/`.

### Tricky Questions

Question: Is this project production-ready in Version 1?

Short answer: No.

Detailed answer: Version 1 is only the foundation. It is production-oriented in structure, but it does not yet implement parsing, embeddings, retrieval, APIs, UI, evaluation, Docker, or AWS deployment.

What not to say: "Yes, it is production-ready."

Red flag to avoid: Overselling the current version.

### System Design Questions

Question: What will the full architecture look like?

Short answer: PDFs will be ingested, chunked, embedded, stored in ChromaDB, retrieved semantically, and used by an LLM to generate cited answers.

Detailed answer: The user will upload or select healthcare PDFs. The ingestion layer will extract text using PyPDF, Unstructured, and OCR fallback. LangChain will convert the content into document objects, split them into chunks, create OpenAI embeddings, and store vectors in ChromaDB. During question answering, the system will retrieve relevant chunks, send them to the LLM, and return an answer with source file names and page numbers. FastAPI will expose the backend, Streamlit will provide the UI, RAGAS will evaluate quality, Docker will package the app, and AWS S3/EC2 will support deployment.

### Resume Defense Questions

Question: Your resume mentions many tools. Are they all implemented now?

Short answer: Not yet in Version 1.

Detailed answer: Version 1 creates the foundation. The project roadmap adds each tool step by step so I can understand, test, and explain every part clearly.

Strong resume-style explanation: "I designed a modular healthcare RAG platform foundation with clear separation between ingestion, retrieval, API, UI, evaluation, and deployment layers."

### Why Did You Choose This Tool Questions

Question: Why use `.env.example`?

Short answer: To document required environment variables without exposing secrets.

Detailed answer: `.env.example` tells developers what configuration values are needed. The real `.env` file stays local and is ignored by Git, which prevents API keys from being uploaded to GitHub.

Question: Why use `.gitignore`?

Short answer: To keep secrets, caches, local data, and generated files out of Git.

### Limitations Questions

Question: What are the limitations of Version 1?

Short answer: It has no runnable RAG functionality yet.

Detailed answer: It does not parse PDFs, create embeddings, store vectors, retrieve documents, generate answers, expose APIs, provide a UI, evaluate quality, or deploy to cloud. It is only the project foundation.

### Production Improvement Questions

Question: How would you improve this foundation for production?

Short answer: Add tests, configuration validation, logging, CI/CD, Docker, cloud storage, and deployment automation.

Detailed answer: I would add typed settings, automated tests, structured logging, a proper API layer, robust error handling, document processing jobs, persistent vector storage, RAGAS evaluation, Docker images, GitHub Actions, S3 document storage, and EC2 deployment.

## Version 2: Basic Python Configuration And Health Check

### 1. What I Built

I added the first small runnable backend layer.

Version 2 includes:
- `backend/__init__.py`
- `backend/app/core/settings.py`
- `backend/app/core/health.py`
- `scripts/health_check.py`
- `tests/test_health.py`
- extra local app settings in `.env.example`
- updated README instructions

### 2. Why I Built It

Before building PDF ingestion or RAG, the backend needs a simple way to load configuration and prove the project is wired correctly.

The health check confirms that:
- Python can import the backend package
- basic settings can be loaded
- important local folders exist
- tests can run successfully

This is a common production habit. Small health checks make it easier to debug bigger systems later.

### 3. What Each File And Folder Does

`backend/__init__.py`

This marks `backend/` as a Python package.

`backend/app/core/settings.py`

This stores application settings such as the app name, version, environment, raw data folder, processed data folder, and ChromaDB folder.

`backend/app/core/health.py`

This contains the health check logic. It returns a dictionary with project status, app metadata, and whether key folders exist.

`scripts/health_check.py`

This is a command-line script. It runs the health check and prints the result in the terminal.

`tests/test_health.py`

This contains automated tests for the settings and health check.

`.env.example`

This now includes safe placeholders for `APP_NAME`, `APP_VERSION`, and `ENVIRONMENT`.

### 4. How The Code Works In Simple Words

`settings.py` creates a small `Settings` object.

That object stores important project paths:
- `data/raw`
- `data/processed`
- `data/vector_db/chroma`

`health.py` asks: "Can I see the important folders?"

Then it returns a result like:

```text
status: ok
app_version: 0.2.0
raw_data_dir exists: true
processed_data_dir exists: true
chroma_db_dir exists: true
```

`scripts/health_check.py` lets me run that check from the terminal.

`tests/test_health.py` proves the settings and health check behave as expected.

### 5. How This Step Connects To The Full RAG Pipeline

The future RAG system will need configuration for:
- where PDFs are stored
- where processed chunks are stored
- where ChromaDB vector files are stored
- which environment is running
- which backend version is active

Version 2 creates the small configuration foundation that later ingestion, retrieval, API, Docker, and AWS code can reuse.

### 6. How This Step Connects To The Resume

This version supports the Python backend foundation of the project.

A clear way to describe this version is:

"I implemented a small backend configuration and health-check layer with unit tests to verify the project structure before adding PDF ingestion and RAG functionality."

### 7. What Changed From Version 1

Version 1 had only folders and documentation.

Version 2 adds real runnable Python code:
- settings loader
- health check function
- command-line script
- automated tests

### 8. What Output I Should Expect

Running:

```bash
python3 scripts/health_check.py
```

should print a dictionary showing:
- status is `ok`
- app version is `0.2.0`
- raw data folder exists
- processed data folder exists
- ChromaDB folder exists

Running:

```bash
python3 -m unittest discover -s tests
```

should show:

```text
Ran 2 tests
OK
```

### 9. Common Mistakes And How To Fix Them

Mistake: Running the script from the wrong folder.

Fix: Run commands from the project root folder: `rag-healthcare`.

Mistake: Seeing `ModuleNotFoundError: No module named 'backend'`.

Fix: Make sure `scripts/health_check.py` adds the project root to `sys.path`, and run the latest version of the file.

Mistake: Expecting this to call OpenAI.

Fix: Version 2 does not call OpenAI. It only checks local project setup.

Mistake: Thinking this is a FastAPI endpoint.

Fix: This is not an API endpoint yet. FastAPI comes later.

### 10. What I Will Build Next

In Version 3, I will add healthcare PDF ingestion using PyPDF.

The next goal is to place a PDF in `data/raw/`, read its pages, extract text, and preserve metadata like file name and page number.

## Version 2 ChatGPT Summary

We completed Version 2 of the Enterprise Healthcare Document Intelligence RAG Platform. Version 2 added a small runnable Python backend foundation, but did not implement PDF ingestion, RAG, embeddings, ChromaDB usage, FastAPI, Streamlit, Docker, AWS, OCR, or RAGAS yet.

Files added include `backend/__init__.py`, `backend/app/core/settings.py`, `backend/app/core/health.py`, `scripts/health_check.py`, and `tests/test_health.py`. The settings file defines local application settings and important data paths. The health file returns a simple status dictionary showing app metadata and whether important folders exist. The script runs the health check from the terminal. The tests verify default settings and health-check behavior.

The health check was verified with `python3 scripts/health_check.py`, which returned status `ok`. Unit tests were verified with `python3 -m unittest discover -s tests`, which ran 2 tests successfully.

## Version 2 Interview Preparation

### Most Likely Interview Questions

Question: What did you build in Version 2?

Short answer: I built the first runnable backend foundation with settings, a health check, a script, and tests.

Detailed answer: I added a small configuration layer to manage app metadata and local data paths. I also added health-check logic that verifies important folders exist, plus unit tests to confirm the setup works.

Follow-up: Why build a health check before RAG?

Answer: A health check proves the application foundation works before adding more complex pieces like PDF parsing, embeddings, retrieval, and APIs.

What not to say: "This is the full backend API."

Red flag to avoid: Claiming this is already FastAPI or production-deployed.

### Theory Questions

Question: What is configuration management?

Short answer: It is how an application manages settings like paths, versions, environments, and secret values.

Detailed answer: Instead of hard-coding values everywhere, configuration keeps important values in one place. This makes the project easier to change between local, Docker, and cloud environments.

### Coding Questions

Question: What does `settings.py` do?

Short answer: It defines and loads app settings.

Detailed answer: It creates a `Settings` object with the app name, version, environment, and local folder paths. Other parts of the backend can reuse those values.

Question: What does `health.py` do?

Short answer: It checks whether the project foundation is working.

Detailed answer: It loads settings and returns a dictionary with app metadata and folder existence checks.

### Tricky Questions

Question: Why did you not use Pydantic settings yet?

Short answer: I kept Version 2 simple and dependency-light.

Detailed answer: Pydantic settings is useful for larger apps, and I may add it later. For this early version, standard library code is enough to teach the concept and avoid unnecessary setup complexity.

### System Design Questions

Question: How does this help the future RAG system?

Short answer: Future RAG components need shared paths and environment settings.

Detailed answer: PDF ingestion will use `data/raw`, processing will use `data/processed`, and vector storage will use `data/vector_db/chroma`. Central settings prevent those paths from being scattered throughout the code.

### Resume Defense Questions

Question: Can you claim RAG is implemented after Version 2?

Short answer: No.

Detailed answer: Version 2 only implements the backend foundation. RAG starts later when PDF ingestion, chunking, embeddings, vector storage, retrieval, and LLM generation are added.

Strong resume-style explanation: "Implemented backend configuration, health-check logic, command-line verification, and unit tests as the foundation for a healthcare RAG platform."

### Why Did You Choose This Tool Questions

Question: Why use Python `unittest`?

Short answer: It works without installing extra packages.

Detailed answer: Since Version 2 is small, Python's built-in testing framework is enough. Later, I can use `pytest` for a richer testing workflow.

### Limitations Questions

Question: What are the limitations of Version 2?

Short answer: It does not process documents or answer questions yet.

Detailed answer: It only checks configuration and folder structure. It does not parse PDFs, call OpenAI, create embeddings, store vectors, retrieve chunks, run FastAPI, or show a UI.

### Production Improvement Questions

Question: How would you improve this in production?

Short answer: Add typed validation, structured logging, real service health endpoints, and CI tests.

Detailed answer: I would use Pydantic settings, validate required environment variables, expose `/health` through FastAPI, add structured logs, add Docker health checks, and run tests automatically in GitHub Actions.

## Version 3: Healthcare PDF Ingestion With PyPDF

### 1. What I Built

I added the first document ingestion layer using PyPDF.

Version 3 includes:
- `backend/app/ingestion/pdf_loader.py`
- `scripts/ingest_pdfs.py`
- `tests/test_pdf_loader.py`
- updated app version `0.3.0`
- updated README instructions

The project can now read PDF files from `data/raw/` and extract page-level text and metadata.

### 2. Why I Built It

RAG starts with documents.

Before chunking, embeddings, vector databases, retrieval, or LLM answers, the system must first load PDFs and extract text.

PyPDF is a good first parser because it is simple and works well for many text-based PDFs. It does not solve every PDF problem, but it is a strong starting point.

### 3. What Each File And Folder Does

`backend/app/ingestion/pdf_loader.py`

This file contains the PDF ingestion logic.

It has:
- `ParsedPDFPage`
- `load_pdf_pages`
- `load_pdfs_from_directory`

`ParsedPDFPage`

This is a small data object that stores one PDF page's text and metadata.

It stores:
- extracted text
- file name
- file path
- page number
- total pages in the PDF

`load_pdf_pages(pdf_path)`

This function reads one PDF file and returns a list of parsed pages.

`load_pdfs_from_directory(directory)`

This function reads every `.pdf` file in a folder and returns all parsed pages.

`scripts/ingest_pdfs.py`

This command-line script loads PDFs from `data/raw/` and prints a short summary.

`tests/test_pdf_loader.py`

This file tests the PDF loader. The tests create temporary PDF files, parse them, and check that metadata is correct.

### 4. How The Code Works In Simple Words

The script starts in `scripts/ingest_pdfs.py`.

It loads settings from `settings.py`.

The settings tell it where raw PDFs live:

```text
data/raw
```

Then it calls:

```text
load_pdfs_from_directory(data/raw)
```

That function finds every `.pdf` file in the folder.

For each PDF, it calls:

```text
load_pdf_pages(pdf_path)
```

PyPDF opens the PDF. The code loops through every page. For each page, it extracts text and saves metadata.

The result is a list of page objects. Each page knows:
- which file it came from
- which page number it came from
- how many pages were in the file
- what text was extracted

### 5. How This Step Connects To The Full RAG Pipeline

This version builds the first real RAG input stage.

The future pipeline will use this extracted text like this:

```text
PDF page text
→ LangChain document object
→ text chunks
→ OpenAI embeddings
→ ChromaDB
→ semantic search
→ grounded LLM answer
→ source citation with file name and page number
```

The file name and page number metadata are very important because citations later depend on them.

### 6. How This Step Connects To The Resume

This version supports the PyPDF and healthcare PDF ingestion part of the project.

A clear way to describe this version is:

"I implemented a PyPDF-based ingestion layer that extracts page-level text from PDFs while preserving file name, file path, page number, and total page metadata for future source citations."

### 7. What Changed From Version 2

Version 2 only checked project health and configuration.

Version 3 adds real document ingestion.

New behavior:
- reads PDF files
- extracts page text
- keeps page metadata
- has tests for PDF parsing behavior
- includes an ingestion command-line script

### 8. What Output I Should Expect

If `data/raw/` is empty, running:

```bash
python3 scripts/ingest_pdfs.py
```

prints:

```text
PDF pages parsed: 0
```

That is correct.

After adding PDFs to `data/raw/`, the script should print one line per parsed page, including:
- file name
- page number
- total pages
- character count
- a short text preview

Running tests:

```bash
python3 -m unittest discover -s tests
```

should show:

```text
Ran 5 tests
OK
```

### 9. Common Mistakes And How To Fix Them

Mistake: Running ingestion and seeing `PDF pages parsed: 0`.

Fix: Put one or more `.pdf` files inside `data/raw/`.

Mistake: Expecting scanned PDFs to produce text.

Fix: PyPDF works best on text-based PDFs. Scanned PDFs usually need OCR, which will come in a later version.

Mistake: Uploading private healthcare PDFs to GitHub.

Fix: Keep PDFs in `data/raw/`. This folder is ignored by Git.

Mistake: Thinking this creates embeddings.

Fix: Version 3 only extracts PDF text. Embeddings come later.

### 10. What I Will Build Next

In Version 4, I will convert extracted PDF pages into LangChain document objects and split text into chunks.

That will prepare the text for embeddings and vector search.

## Version 3 ChatGPT Summary

We completed Version 3 of the Enterprise Healthcare Document Intelligence RAG Platform. Version 3 added PyPDF-based PDF ingestion. It did not implement Unstructured, OCR, LangChain document objects, text splitting, embeddings, ChromaDB vector writes, retrieval, LLM answering, FastAPI, Streamlit, Docker, AWS, or RAGAS yet.

Files added include `backend/app/ingestion/pdf_loader.py`, `scripts/ingest_pdfs.py`, and `tests/test_pdf_loader.py`. The PDF loader defines a `ParsedPDFPage` object that stores extracted page text plus metadata: file name, file path, page number, and total pages. The loader can parse one PDF or all PDFs in a directory. The ingestion script reads PDFs from `data/raw/` and prints a summary. The tests create temporary PDFs and verify parsing and metadata behavior.

The project version was updated to `0.3.0`. Tests were verified with `python3 -m unittest discover -s tests`, which ran 5 tests successfully. The ingestion script was verified with `python3 scripts/ingest_pdfs.py`; because `data/raw/` is currently empty, it correctly reported `PDF pages parsed: 0`.

## Version 3 Interview Preparation

### Most Likely Interview Questions

Question: What did you build in Version 3?

Short answer: I built a PyPDF-based PDF ingestion layer.

Detailed answer: I implemented code that reads PDFs, extracts text page by page, and preserves metadata such as file name, file path, page number, and total page count. This metadata will later support source citations in the RAG answer.

Follow-up: Why is page-level metadata important?

Answer: Because citations need to show where an answer came from. If I keep file name and page number during ingestion, I can carry that metadata through chunking, retrieval, and answer generation.

What not to say: "This handles every kind of PDF perfectly."

Red flag to avoid: Ignoring scanned PDFs and OCR limitations.

### Theory Questions

Question: What is PDF ingestion?

Short answer: It is the process of loading PDFs and extracting useful text and metadata.

Detailed answer: In a RAG system, ingestion is the first step. The system reads source documents, extracts text, preserves metadata, and prepares the content for chunking and embedding.

Question: Why does RAG need ingestion?

Short answer: The system needs document text before it can search or answer questions.

Detailed answer: Without ingestion, there is no source text to chunk, embed, retrieve, or cite.

### Coding Questions

Question: What does `load_pdf_pages` return?

Short answer: It returns a list of parsed PDF page objects.

Detailed answer: Each object contains the extracted text and metadata for one page, including file name, file path, page number, and total pages.

Question: Why did you validate that the file ends with `.pdf`?

Short answer: To catch incorrect inputs early.

Detailed answer: If someone passes a text file or another unsupported file type, the function raises a clear error instead of failing in a confusing way inside PyPDF.

### Tricky Questions

Question: Can PyPDF read scanned PDFs?

Short answer: Usually no.

Detailed answer: PyPDF extracts embedded text. If a PDF page is just an image scan, there may be no embedded text to extract. For scanned PDFs, OCR is needed.

Question: Why not use Unstructured first?

Short answer: PyPDF is simpler for the first ingestion version.

Detailed answer: PyPDF is a lightweight starting point for text-based PDFs. Unstructured is useful for more complex layouts and will be added later so I can compare and explain both approaches.

### System Design Questions

Question: Where does this fit in the RAG architecture?

Short answer: It is the first ingestion step.

Detailed answer: PDFs enter the system through this loader. The extracted pages will later become LangChain documents, then chunks, then embeddings, then ChromaDB records for retrieval.

### Resume Defense Questions

Question: Your resume says healthcare PDF ingestion. What does that mean here?

Short answer: I implemented a PDF ingestion layer that can read healthcare PDFs from a local raw data folder and preserve page-level metadata.

Detailed answer: The ingestion module uses PyPDF to load PDF files from `data/raw/`, extract text page by page, and preserve metadata needed for traceability and citations.

Strong resume-style explanation: "Built a PyPDF ingestion layer for healthcare PDFs with page-level extraction and metadata preservation for downstream RAG citations."

### Why Did You Choose This Tool Questions

Question: Why PyPDF?

Short answer: It is simple and effective for text-based PDFs.

Detailed answer: PyPDF is lightweight and easy to use for extracting text from many PDFs. It is a good first parser before adding more advanced parsing with Unstructured and OCR fallback.

### Limitations Questions

Question: What are the limitations of Version 3?

Short answer: It only handles basic text extraction from PDFs.

Detailed answer: It does not handle OCR for scanned documents, advanced tables, complex layouts, semantic chunking, embeddings, retrieval, or answer generation yet.

### Production Improvement Questions

Question: How would you improve PDF ingestion in production?

Short answer: Add validation, OCR, better layout parsing, logging, retries, and document status tracking.

Detailed answer: I would add file type validation, corrupted PDF handling, OCR fallback, Unstructured parsing for complex layouts, page-level processing logs, S3 document storage, ingestion job tracking, duplicate detection, and automated tests with realistic sample PDFs.

## Version 4: LangChain Documents And Text Splitting

### 1. What I Built

I added the LangChain document preparation layer.

Version 4 includes:
- `backend/app/rag/document_processing.py`
- `scripts/chunk_pdfs.py`
- `tests/test_document_processing.py`
- `CHUNK_SIZE` and `CHUNK_OVERLAP` settings
- app version `0.4.0`
- updated README instructions

The project can now convert parsed PDF pages into LangChain `Document` objects and split those documents into smaller text chunks.

### 2. Why I Built It

LLMs and embedding models should not receive entire long PDFs at once.

A RAG system usually breaks documents into smaller chunks so the retriever can search focused pieces of text.

This version prepares text for the next step: embeddings.

### 3. What Each File And Folder Does

`backend/app/rag/document_processing.py`

This contains the RAG preparation logic.

It has:
- `pages_to_documents`
- `split_documents`

`pages_to_documents`

This converts parsed PDF pages into LangChain `Document` objects.

Each LangChain document has:
- `page_content`: the text
- `metadata`: file name, file path, page number, and total pages

`split_documents`

This uses LangChain's `RecursiveCharacterTextSplitter` to split long documents into smaller chunks.

Each chunk keeps the original citation metadata and adds:
- `chunk_number`
- `chunk_id`

`scripts/chunk_pdfs.py`

This script runs the Version 4 pipeline from the terminal:

```text
PDFs -> parsed pages -> LangChain documents -> text chunks
```

`tests/test_document_processing.py`

This tests document conversion, metadata preservation, empty-text handling, chunk creation, and invalid chunk settings.

### 4. How The Code Works In Simple Words

Version 3 produced parsed PDF pages.

Version 4 takes those pages and turns them into LangChain documents.

A LangChain document is like a small container with two parts:

```text
page_content = the actual text
metadata = where the text came from
```

Then the text splitter breaks long text into smaller pieces.

For example:

```text
one long page
-> chunk 1
-> chunk 2
-> chunk 3
```

Each chunk still remembers the original file name and page number.

### 5. How This Step Connects To The Full RAG Pipeline

This is the bridge between PDF ingestion and embeddings.

The pipeline now looks like:

```text
PDF
-> PyPDF page extraction
-> LangChain Document objects
-> text chunks
-> future OpenAI embeddings
-> future ChromaDB vector storage
-> future semantic retrieval
-> future grounded answer with citations
```

### 6. How This Step Connects To The Resume

This version supports the LangChain document and text splitting part of the resume stack.

A clear way to describe this version is:

"I converted extracted PDF pages into LangChain Document objects and used RecursiveCharacterTextSplitter to create citation-ready chunks with preserved file and page metadata."

### 7. What Changed From Version 3

Version 3 extracted page text with PyPDF.

Version 4 prepares that text for RAG:
- converts pages into LangChain documents
- splits documents into chunks
- preserves metadata for citations
- adds chunk IDs for future vector storage
- adds chunking tests

### 8. What Output I Should Expect

If `data/raw/` is empty, running:

```bash
python3 scripts/chunk_pdfs.py
```

prints:

```text
PDF pages parsed: 0
LangChain documents created: 0
Text chunks created: 0
```

That is correct.

After PDFs are added to `data/raw/`, the script should show how many pages, documents, and chunks were created.

Running tests:

```bash
python3 -m unittest discover -s tests
```

should show:

```text
Ran 9 tests
OK
```

### 9. Common Mistakes And How To Fix Them

Mistake: Expecting chunks when `data/raw/` has no PDFs.

Fix: Add a PDF to `data/raw/`.

Mistake: Expecting chunks from scanned PDFs.

Fix: Scanned PDFs may have no extractable text. OCR comes later.

Mistake: Setting `CHUNK_OVERLAP` bigger than `CHUNK_SIZE`.

Fix: Keep overlap smaller than chunk size.

Mistake: Thinking chunks are embeddings.

Fix: Chunks are still text. Embeddings come in Version 5.

### 10. What I Will Build Next

In Version 5, I will add OpenAI embeddings and ChromaDB storage.

That means the text chunks will be converted into vectors and saved in the local vector database folder.

## Version 4 ChatGPT Summary

We completed Version 4 of the Enterprise Healthcare Document Intelligence RAG Platform. Version 4 added LangChain Document conversion and recursive text splitting. It did not implement OpenAI embeddings, ChromaDB vector writes, semantic retrieval, LLM answering, FastAPI, Streamlit, Unstructured, OCR, Docker, AWS, or RAGAS yet.

Files added include `backend/app/rag/document_processing.py`, `scripts/chunk_pdfs.py`, and `tests/test_document_processing.py`. The document processing module converts parsed PDF pages into LangChain `Document` objects, preserving metadata such as file name, file path, page number, and total pages. It also splits documents into smaller chunks using `RecursiveCharacterTextSplitter`, preserving citation metadata and adding `chunk_number` and `chunk_id`.

The app version was updated to `0.4.0`. `CHUNK_SIZE` and `CHUNK_OVERLAP` were added to `.env.example` and settings. Tests were verified with `python3 -m unittest discover -s tests`, which ran 9 tests successfully. The chunking script was verified with `python3 scripts/chunk_pdfs.py`; because `data/raw/` is empty, it correctly reported 0 pages, 0 LangChain documents, and 0 chunks.

## Version 4 Interview Preparation

### Most Likely Interview Questions

Question: What did you build in Version 4?

Short answer: I converted parsed PDF pages into LangChain documents and split them into chunks.

Detailed answer: I added a RAG preparation layer that takes page-level text from PyPDF, creates LangChain `Document` objects, preserves citation metadata, and uses RecursiveCharacterTextSplitter to create smaller chunks for future embeddings.

Follow-up: Why do chunks need metadata?

Answer: Because retrieval returns chunks, and each chunk needs to know which source file and page it came from so the final answer can show citations.

What not to say: "Chunking creates embeddings."

Red flag to avoid: Confusing chunks with vectors.

### Theory Questions

Question: What is a LangChain Document?

Short answer: It is a standard object that stores text and metadata.

Detailed answer: A LangChain `Document` has `page_content` for the actual text and `metadata` for information like file name, page number, source path, or document type.

Question: Why split text?

Short answer: Smaller chunks are easier to search and fit into model context windows.

Detailed answer: Long documents may contain many topics. Splitting creates focused text units that can be embedded and retrieved more accurately.

### Coding Questions

Question: What does `pages_to_documents` do?

Short answer: It turns parsed PDF pages into LangChain documents.

Detailed answer: It copies the extracted page text into `page_content` and stores file/page metadata in the document metadata.

Question: What does `split_documents` do?

Short answer: It splits LangChain documents into smaller chunks.

Detailed answer: It uses RecursiveCharacterTextSplitter and adds chunk-level metadata like `chunk_number` and `chunk_id`.

### Tricky Questions

Question: What happens to empty pages?

Short answer: Empty pages are skipped.

Detailed answer: Empty text is not useful for embeddings or retrieval. Later, OCR fallback can handle scanned pages that PyPDF could not read.

Question: Why RecursiveCharacterTextSplitter?

Short answer: It is a common LangChain splitter that tries to keep text boundaries natural.

Detailed answer: It recursively splits by larger separators first, then smaller ones, which usually creates cleaner chunks than cutting text at random character positions.

### System Design Questions

Question: Where does chunking fit in the RAG system?

Short answer: Between document ingestion and embeddings.

Detailed answer: PDF parsing extracts raw text. Chunking prepares that text into smaller units. Embedding then converts each chunk into a vector for ChromaDB storage and semantic search.

### Resume Defense Questions

Question: Your resume mentions LangChain. What part uses LangChain here?

Short answer: Version 4 uses LangChain `Document` objects and RecursiveCharacterTextSplitter.

Detailed answer: I use LangChain to standardize document representation and chunking before embeddings and vector database storage.

Strong resume-style explanation: "Implemented LangChain-based document conversion and recursive text splitting with citation metadata preservation for downstream RAG retrieval."

### Why Did You Choose This Tool Questions

Question: Why LangChain documents?

Short answer: They provide a standard text-plus-metadata format for RAG pipelines.

Detailed answer: LangChain documents make it easier to connect ingestion, splitting, embeddings, vector stores, and retrievers because many LangChain components expect this format.

### Limitations Questions

Question: What are the limitations of Version 4?

Short answer: It prepares chunks but does not search or answer yet.

Detailed answer: It does not create embeddings, store vectors, retrieve semantically, call an LLM, handle OCR, or expose an API/UI.

### Production Improvement Questions

Question: How would you improve chunking in production?

Short answer: Tune chunk sizes, use document-aware splitting, evaluate retrieval quality, and track chunk lineage.

Detailed answer: I would test different chunk sizes and overlaps, use structure-aware chunking for headings/tables, evaluate retrieval with RAGAS, store stable chunk IDs, track document versions, and monitor which chunks are used in answers.

## Version 5: OpenAI Embeddings And ChromaDB Storage

### 1. What I Built

I added the vector storage layer.

Version 5 includes:
- `backend/app/rag/vector_store.py`
- `scripts/build_vector_store.py`
- `tests/test_vector_store.py`
- OpenAI embedding model setting
- ChromaDB collection setting
- automatic local `.env` loading
- app version `0.5.0`

The project can now take text chunks and store them in a local ChromaDB vector database using embeddings.

### 2. Why I Built It

Chunking creates text pieces, but semantic search needs vectors.

An embedding model converts text into numbers. ChromaDB stores those numbers so the system can later search by meaning instead of only exact words.

### 3. What Each File Does

`backend/app/rag/vector_store.py`

This contains vector database logic.

It has:
- `create_openai_embeddings`
- `create_chroma_vector_store`
- `store_documents_in_chroma`

`create_openai_embeddings`

This creates the real OpenAI embedding client using the configured embedding model.

It requires `OPENAI_API_KEY` from the local environment or local `.env` file.

`create_chroma_vector_store`

This creates or loads a persistent ChromaDB collection.

`store_documents_in_chroma`

This embeds chunks and stores them in ChromaDB.

`scripts/build_vector_store.py`

This runs the full local pipeline:

```text
PDFs -> pages -> LangChain documents -> chunks -> OpenAI embeddings -> ChromaDB
```

`tests/test_vector_store.py`

This tests vector storage using fake local embeddings, so tests do not call OpenAI and do not need a real API key.

### 4. How The Code Works In Simple Words

The script starts by loading PDFs from `data/raw/`.

Then it:
- extracts PDF pages
- creates LangChain documents
- splits documents into chunks
- creates an OpenAI embedding client
- stores chunks in ChromaDB

Each chunk keeps metadata like:
- file name
- page number
- chunk ID

That metadata is important because search results later need citations.

### 5. How This Step Connects To The Full RAG Pipeline

The pipeline now reaches vector storage:

```text
PDF
-> PyPDF extraction
-> LangChain documents
-> text chunks
-> OpenAI embeddings
-> ChromaDB vector database
```

The next step is retrieval:

```text
user question
-> embed question
-> search ChromaDB
-> return relevant chunks
```

### 6. How This Step Connects To The Resume

This version supports the OpenAI API, embeddings, and ChromaDB parts of the project.

A clear way to describe this version is:

"I implemented an embeddings and vector storage layer using OpenAI embeddings and ChromaDB, while preserving citation metadata for downstream semantic retrieval."

### 7. What Changed From Version 4

Version 4 created chunks.

Version 5 stores chunks in a vector database.

New behavior:
- OpenAI embedding client setup
- ChromaDB collection setup
- vector database persistence path
- fake embedding tests for safe local verification
- `.env` loading for local secrets

### 8. What Output I Should Expect

If `data/raw/` is empty, running:

```bash
python3 scripts/build_vector_store.py
```

prints:

```text
PDF pages parsed: 0
LangChain documents created: 0
Text chunks created: 0
No chunks found. Add text-based PDFs to data/raw before embedding.
```

That is correct.

If PDFs exist and chunks are created, the script will need a real local `OPENAI_API_KEY` in `.env`.

Running tests:

```bash
python3 -m unittest discover -s tests
```

should show:

```text
Ran 12 tests
OK
```

### 9. Common Mistakes And How To Fix Them

Mistake: Pasting an API key into chat.

Fix: Never paste keys into chat. Put the key only in a local `.env` file.

Mistake: Committing `.env`.

Fix: `.env` is ignored by Git. Keep it that way.

Mistake: Running vector store build with PDFs but no API key.

Fix: Create a local `.env` file with `OPENAI_API_KEY=...`.

Mistake: Thinking ChromaDB is retrieval by itself.

Fix: ChromaDB stores and searches vectors. The retrieval logic will be built in the next version.

### 10. What I Will Build Next

In Version 6, I will add semantic retrieval.

That means a user question will search ChromaDB and return the most relevant chunks with metadata.

## Version 5 ChatGPT Summary

We completed Version 5 of the Enterprise Healthcare Document Intelligence RAG Platform. Version 5 added OpenAI embedding client setup and local ChromaDB vector storage. It did not implement semantic retrieval, LLM answer generation, FastAPI, Streamlit, Unstructured, OCR, Docker, AWS, or RAGAS yet.

Files added include `backend/app/rag/vector_store.py`, `scripts/build_vector_store.py`, and `tests/test_vector_store.py`. The vector store module creates an OpenAI embedding client, creates or loads a persistent ChromaDB collection, and stores chunk documents in ChromaDB. The build script runs the pipeline from PDFs to chunks to embeddings to ChromaDB. Tests use fake deterministic embeddings so they do not call OpenAI or require a real API key.

The app version was updated to `0.5.0`. Settings now include `EMBEDDING_MODEL=text-embedding-3-small` and `CHROMA_COLLECTION_NAME=healthcare_documents`. Local `.env` loading was added so real secrets can stay on the machine and out of GitHub. Tests were verified with `python3 -m unittest discover -s tests`, which ran 12 tests successfully. The vector build script was verified with `python3 scripts/build_vector_store.py`; because `data/raw/` is empty, it safely reported no chunks and made no OpenAI call.

## Version 5 Interview Preparation

### Most Likely Interview Questions

Question: What did you build in Version 5?

Short answer: I added OpenAI embeddings and ChromaDB vector storage.

Detailed answer: I implemented a vector storage layer that can embed chunked documents using OpenAI embeddings and store them in a persistent local ChromaDB collection with citation metadata.

Follow-up: Did your tests call OpenAI?

Answer: No. Tests use fake deterministic embeddings so they are fast, free, and safe.

What not to say: "I put my API key in the code."

Red flag to avoid: Hard-coding secrets.

### Theory Questions

Question: What is an embedding?

Short answer: An embedding is a numeric representation of text.

Detailed answer: Embeddings convert text into vectors so similar meanings are close together mathematically. This allows semantic search.

Question: What is a vector database?

Short answer: It stores embeddings and searches for similar vectors.

Detailed answer: ChromaDB stores chunk embeddings and metadata. Later, when a user asks a question, the question is embedded and compared to stored chunk vectors.

### Coding Questions

Question: What does `store_documents_in_chroma` do?

Short answer: It stores chunk documents in ChromaDB using an embedding model.

Detailed answer: It creates or loads a ChromaDB collection, generates embeddings through the embedding function, stores the documents, and uses chunk IDs as stable document IDs.

Question: Why use fake embeddings in tests?

Short answer: To test vector database behavior without external API calls.

Detailed answer: Unit tests should be reliable and cheap. Fake embeddings let me verify storage and search behavior without needing network access or OpenAI billing.

### Tricky Questions

Question: Is ChromaDB the same as OpenAI embeddings?

Short answer: No.

Detailed answer: OpenAI creates embeddings. ChromaDB stores and searches those embeddings.

Question: Does this version answer questions?

Short answer: No.

Detailed answer: Version 5 stores vectors. Version 6 will retrieve relevant chunks. LLM answer generation comes later.

### System Design Questions

Question: Where does ChromaDB fit in the architecture?

Short answer: After chunking and embedding.

Detailed answer: Chunks are embedded into vectors and saved in ChromaDB. During retrieval, the user query will also be embedded and matched against stored vectors.

### Resume Defense Questions

Question: Your resume mentions OpenAI API and ChromaDB. What did you implement?

Short answer: I implemented an embedding and vector storage layer using OpenAI embeddings and ChromaDB.

Detailed answer: The project can create embeddings for chunks and persist them in a ChromaDB collection while preserving metadata for citations.

Strong resume-style explanation: "Implemented OpenAI embedding integration and ChromaDB vector persistence for healthcare document chunks with citation metadata."

### Why Did You Choose This Tool Questions

Question: Why ChromaDB?

Short answer: It is simple, local-friendly, and works well for learning and prototypes.

Detailed answer: ChromaDB is easy to persist locally, integrates with LangChain, and is good for developing a RAG workflow before moving to a managed vector database in production.

### Limitations Questions

Question: What are the limitations of Version 5?

Short answer: It stores vectors but does not retrieve or answer yet.

Detailed answer: It does not implement semantic retrieval logic, LLM generation, citation formatting, API endpoints, UI, OCR, or production deployment.

### Production Improvement Questions

Question: How would you improve this in production?

Short answer: Add batch jobs, idempotent indexing, monitoring, retries, and managed vector storage.

Detailed answer: I would add ingestion job tracking, duplicate detection, document versioning, batch embedding, retry handling, cost monitoring, vector index rebuild workflows, access controls, and possibly a managed vector database depending on scale.

## Version 6: Semantic Retrieval From ChromaDB

### 1. What I Built

I added semantic retrieval.

Version 6 includes:
- `backend/app/rag/retriever.py`
- `scripts/search_vector_store.py`
- `tests/test_retriever.py`
- `RETRIEVAL_TOP_K` setting
- app version `0.6.0`

The project can now search a ChromaDB vector store and return the most relevant chunks with citation metadata.

### 2. Why I Built It

Version 5 stored chunks as vectors.

Version 6 retrieves relevant chunks for a user question.

This is the "R" in RAG: retrieval.

### 3. What Each File Does

`backend/app/rag/retriever.py`

This contains the semantic retrieval logic.

It has:
- `RetrievedChunk`
- `retrieve_relevant_chunks`

`RetrievedChunk`

This is a small result object for one retrieved chunk.

It stores:
- chunk text
- similarity score
- file name
- page number
- chunk ID
- full metadata

`retrieve_relevant_chunks`

This searches ChromaDB for chunks that are semantically similar to a query.

`scripts/search_vector_store.py`

This lets me search the local vector database from the terminal.

Example:

```bash
python3 scripts/search_vector_store.py "What does the document say about diabetes?"
```

`tests/test_retriever.py`

This verifies retrieval behavior using fake local embeddings, so tests do not call OpenAI.

### 4. How The Code Works In Simple Words

The user provides a question.

The retriever opens the ChromaDB collection.

ChromaDB compares the question embedding against stored chunk embeddings.

It returns the most similar chunks.

The code converts those raw LangChain search results into clean `RetrievedChunk` objects.

Each result keeps source information:
- file name
- page number
- chunk ID

### 5. How This Step Connects To The Full RAG Pipeline

The pipeline now has retrieval:

```text
PDF
-> PyPDF extraction
-> LangChain documents
-> text chunks
-> OpenAI embeddings
-> ChromaDB vector database
-> semantic retrieval
```

The next step is answer generation:

```text
retrieved chunks
-> LLM prompt
-> grounded answer
-> source citations
```

### 6. How This Step Connects To The Resume

This version supports semantic retrieval and vector search in the RAG pipeline.

A clear way to describe this version is:

"I implemented semantic retrieval over ChromaDB, returning relevant healthcare document chunks with file name, page number, chunk ID, and similarity score metadata."

### 7. What Changed From Version 5

Version 5 stored vectors.

Version 6 searches those vectors.

New behavior:
- accepts a user query
- searches ChromaDB
- returns top matching chunks
- preserves citation metadata in retrieval results
- validates empty queries and invalid `top_k`

### 8. What Output I Should Expect

Running without a question:

```bash
python3 scripts/search_vector_store.py
```

prints:

```text
Usage: python3 scripts/search_vector_store.py "your question"
```

That is correct.

Real search requires:
- PDFs in `data/raw/`
- real embeddings stored in ChromaDB
- local `.env` with `OPENAI_API_KEY`

Running tests:

```bash
python3 -m unittest discover -s tests
```

should show:

```text
Ran 15 tests
OK
```

### 9. Common Mistakes And How To Fix Them

Mistake: Running search before building the vector store.

Fix: Run `python3 scripts/build_vector_store.py` first after adding PDFs and a local API key.

Mistake: Expecting retrieval to generate an answer.

Fix: Retrieval only returns source chunks. LLM answer generation comes next.

Mistake: Thinking a lower or higher score always means the same thing across all vector databases.

Fix: Treat scores as ranking signals and understand how the vector store reports distance or similarity.

Mistake: Using a vague query.

Fix: Ask a specific question so retrieval has a better signal.

### 10. What I Will Build Next

In Version 7, I will add grounded LLM answer generation with citations.

That means the system will use retrieved chunks as context and generate an answer that cites file name and page number.

## Version 6 ChatGPT Summary

We completed Version 6 of the Enterprise Healthcare Document Intelligence RAG Platform. Version 6 added semantic retrieval from ChromaDB. It did not implement LLM answer generation, FastAPI, Streamlit, Unstructured, OCR, Docker, AWS, or RAGAS yet.

Files added include `backend/app/rag/retriever.py`, `scripts/search_vector_store.py`, and `tests/test_retriever.py`. The retriever module searches a ChromaDB vector store using an embedding model and returns `RetrievedChunk` objects with text, score, file name, page number, chunk ID, and metadata. The search script lets a user search the local vector store from the terminal. Tests use fake deterministic embeddings, so they do not call OpenAI or require a real API key.

The app version was updated to `0.6.0`. Settings now include `RETRIEVAL_TOP_K=4`. Tests were verified with `python3 -m unittest discover -s tests`, which ran 15 tests successfully. The search script usage was verified with `python3 scripts/search_vector_store.py`, which correctly printed the usage message when no question was provided.

## Version 6 Interview Preparation

### Most Likely Interview Questions

Question: What did you build in Version 6?

Short answer: I built semantic retrieval from ChromaDB.

Detailed answer: I added a retriever that takes a query, searches the ChromaDB vector store, and returns the most relevant document chunks with citation metadata such as file name, page number, and chunk ID.

Follow-up: Does this answer the user's question?

Answer: Not yet. Version 6 retrieves evidence. Version 7 will use that evidence to generate a grounded answer.

What not to say: "This is the full RAG answer generator."

Red flag to avoid: Confusing retrieval with generation.

### Theory Questions

Question: What is semantic retrieval?

Short answer: It searches by meaning instead of exact words.

Detailed answer: The query is converted into an embedding and compared with stored chunk embeddings. Chunks with similar meaning are returned even if they do not use the exact same words.

Question: Why is retrieval important in RAG?

Short answer: It gives the LLM relevant evidence.

Detailed answer: Without retrieval, the LLM may rely on general knowledge or hallucinate. Retrieval provides source-specific context.

### Coding Questions

Question: What does `retrieve_relevant_chunks` do?

Short answer: It searches ChromaDB and returns relevant chunks.

Detailed answer: It validates the query and `top_k`, opens the ChromaDB collection with an embedding function, runs similarity search, and converts results into `RetrievedChunk` objects.

Question: Why return a custom `RetrievedChunk` object?

Short answer: To make retrieval results easier to use later.

Detailed answer: It gives the next layer a clean structure with text, score, file name, page number, chunk ID, and metadata.

### Tricky Questions

Question: Does a retrieved chunk always mean the answer is correct?

Short answer: No.

Detailed answer: Retrieval can return imperfect matches. The answer generation layer must still use the evidence carefully and cite sources.

Question: What does `top_k` mean?

Short answer: It controls how many chunks are returned.

Detailed answer: If `top_k=4`, the retriever returns the four closest chunks according to vector similarity or distance.

### System Design Questions

Question: Where does retrieval fit in the architecture?

Short answer: After vector storage and before LLM generation.

Detailed answer: Chunks are embedded and stored in ChromaDB. When a question arrives, retrieval finds the most relevant chunks. Those chunks are then passed to the LLM in the next version.

### Resume Defense Questions

Question: Your resume mentions semantic retrieval. What did you implement?

Short answer: I implemented a ChromaDB retriever that returns relevant chunks with source metadata.

Detailed answer: The retriever searches the vector database using query embeddings and returns citation-ready chunks with file name, page number, chunk ID, and score.

Strong resume-style explanation: "Implemented semantic retrieval over ChromaDB to return citation-ready healthcare document chunks for downstream grounded answer generation."

### Why Did You Choose This Tool Questions

Question: Why use ChromaDB for retrieval?

Short answer: It integrates well with LangChain and is easy to run locally.

Detailed answer: ChromaDB supports persistent local vector storage and similarity search, which makes it practical for building and explaining a RAG prototype.

### Limitations Questions

Question: What are the limitations of Version 6?

Short answer: It retrieves chunks but does not generate answers.

Detailed answer: It does not create final natural-language answers, enforce answer grounding, format citations, expose an API, or provide a UI.

### Production Improvement Questions

Question: How would you improve retrieval in production?

Short answer: Add reranking, filters, better chunking, monitoring, and retrieval evaluation.

Detailed answer: I would add metadata filters, hybrid keyword/vector search, reranking, query rewriting, access control, retrieval metrics, RAGAS evaluation, and monitoring for missed or irrelevant retrieval results.

## Version 7: Grounded LLM Answer Generation With Citations

### 1. What I Built

I added grounded answer generation.

Version 7 includes:
- `backend/app/rag/answer_generator.py`
- `scripts/answer_question.py`
- `tests/test_answer_generator.py`
- `CHAT_MODEL` setting
- `CHAT_TEMPERATURE` setting
- app version `0.7.0`

The project can now take retrieved chunks and generate an answer with source citations.

### 2. Why I Built It

Retrieval gives evidence, but users usually want an answer.

This version adds the generation step in RAG. The answer generator uses retrieved chunks as context and tells the LLM to answer only from those chunks.

### 3. What Each File Does

`backend/app/rag/answer_generator.py`

This contains grounded answer generation logic.

It has:
- `SourceCitation`
- `GroundedAnswer`
- `create_chat_llm`
- `build_context`
- `build_grounded_prompt`
- `generate_grounded_answer`

`SourceCitation`

This stores citation metadata for one source:
- file name
- page number
- chunk ID

`GroundedAnswer`

This stores the generated answer and the list of citations.

`create_chat_llm`

This creates the real OpenAI chat model client. It requires a local `OPENAI_API_KEY`.

`build_context`

This formats retrieved chunks into a source-aware context block for the LLM.

`build_grounded_prompt`

This creates the prompt that tells the LLM to answer only from retrieved context.

`generate_grounded_answer`

This generates the final answer and returns citations.

`scripts/answer_question.py`

This command-line script runs:

```text
question -> retrieve chunks -> generate grounded answer -> print citations
```

`tests/test_answer_generator.py`

This tests answer generation using a fake local LLM, so tests do not call OpenAI.

### 4. How The Code Works In Simple Words

The retriever returns chunks.

Each chunk has:
- text
- file name
- page number
- chunk ID

The answer generator formats those chunks into context.

Then it builds a prompt that says:
- use only the retrieved source context
- say when the answer is not available
- cite file name and page number

The LLM produces an answer. The code returns the answer plus structured citations.

### 5. How This Step Connects To The Full RAG Pipeline

The core RAG pipeline now exists:

```text
PDF
-> PyPDF extraction
-> LangChain documents
-> text chunks
-> OpenAI embeddings
-> ChromaDB vector database
-> semantic retrieval
-> grounded LLM answer
-> source citations
```

The next step is exposing this through an API.

### 6. How This Step Connects To The Resume

This version supports grounded LLM answer generation and source citations.

A clear way to describe this version is:

"I implemented grounded answer generation over retrieved healthcare document chunks, with structured citations that preserve file name, page number, and chunk ID."

### 7. What Changed From Version 6

Version 6 retrieved relevant chunks.

Version 7 uses retrieved chunks to generate a final answer.

New behavior:
- builds context from retrieved chunks
- creates a grounded prompt
- calls a chat LLM when configured
- returns answer text
- returns structured source citations
- handles no-context cases

### 8. What Output I Should Expect

Running without a question:

```bash
python3 scripts/answer_question.py
```

prints:

```text
Usage: python3 scripts/answer_question.py "your question"
```

That is correct.

Real answering requires:
- PDFs in `data/raw/`
- real embeddings stored in ChromaDB
- local `.env` with `OPENAI_API_KEY`

Running tests:

```bash
python3 -m unittest discover -s tests
```

should show:

```text
Ran 22 tests
OK
```

### 9. Common Mistakes And How To Fix Them

Mistake: Expecting answers before building the vector store.

Fix: Add PDFs, add local `.env`, and run `python3 scripts/build_vector_store.py` first.

Mistake: Thinking citations guarantee correctness.

Fix: Citations show where the answer came from, but the retrieved text and generated answer still need evaluation.

Mistake: Letting the LLM answer from general knowledge.

Fix: The prompt tells the LLM to use only retrieved context.

Mistake: Pasting the API key into chat.

Fix: Keep keys only in local `.env`.

### 10. What I Will Build Next

In Version 8, I will add a FastAPI backend.

That means the RAG pipeline can be called through HTTP endpoints instead of only command-line scripts.

## Version 7 ChatGPT Summary

We completed Version 7 of the Enterprise Healthcare Document Intelligence RAG Platform. Version 7 added grounded LLM answer generation with source citations. It did not implement FastAPI, Streamlit, Unstructured, OCR, Docker, AWS, or RAGAS yet.

Files added include `backend/app/rag/answer_generator.py`, `scripts/answer_question.py`, and `tests/test_answer_generator.py`. The answer generator formats retrieved chunks into citation-aware context, builds a grounded prompt, calls a chat LLM when configured, and returns a `GroundedAnswer` with answer text and structured citations. Citations include file name, page number, and chunk ID. Tests use a fake local LLM, so they do not call OpenAI or require a real API key.

The app version was updated to `0.7.0`. Settings now include `CHAT_MODEL=gpt-4o-mini` and `CHAT_TEMPERATURE=0`. Tests were verified with `python3 -m unittest discover -s tests`, which ran 22 tests successfully. The answer script usage was verified with `python3 scripts/answer_question.py`, which correctly printed the usage message when no question was provided.

## Version 7 Interview Preparation

### Most Likely Interview Questions

Question: What did you build in Version 7?

Short answer: I built grounded LLM answer generation with citations.

Detailed answer: I added an answer generator that takes retrieved chunks, builds a grounded prompt, calls a chat model, and returns an answer with source citations containing file name, page number, and chunk ID.

Follow-up: What does grounded mean?

Answer: It means the answer is based on retrieved source context instead of the LLM answering freely from memory.

What not to say: "The model can never hallucinate now."

Red flag to avoid: Claiming grounding completely eliminates hallucinations.

### Theory Questions

Question: What is answer generation in RAG?

Short answer: It is the generation step where the LLM writes an answer using retrieved evidence.

Detailed answer: Retrieval finds relevant chunks. Generation uses those chunks as context and produces a user-facing answer.

Question: Why are citations important?

Short answer: They make the answer traceable.

Detailed answer: Citations let users see which file and page supported the answer, which is especially important in healthcare document workflows.

### Coding Questions

Question: What does `generate_grounded_answer` do?

Short answer: It generates an answer from retrieved chunks.

Detailed answer: It validates the question, handles no-context cases, builds a grounded prompt, calls either a real LLM or fake test LLM, and returns answer text plus citations.

Question: Why use a fake LLM in tests?

Short answer: To test logic without external API calls.

Detailed answer: Tests should be reliable, fast, and free. A fake LLM lets me verify prompting and citation behavior without using OpenAI.

### Tricky Questions

Question: Does grounding guarantee the answer is correct?

Short answer: No.

Detailed answer: Grounding reduces hallucination risk, but retrieval can be incomplete and the LLM can still misunderstand context. Evaluation is still needed.

Question: What happens when no chunks are retrieved?

Short answer: The system says the documents do not contain enough information.

Detailed answer: It avoids fabricating an answer when there is no source context.

### System Design Questions

Question: Where does answer generation fit in the architecture?

Short answer: After retrieval.

Detailed answer: The system retrieves relevant chunks from ChromaDB, then sends those chunks to the LLM as context for grounded answer generation.

### Resume Defense Questions

Question: Your resume mentions grounded LLM answer generation. What did you implement?

Short answer: I implemented an answer generator that uses retrieved healthcare document chunks as context and returns citations.

Detailed answer: The answer generator builds a source-aware prompt from retrieved chunks and returns structured citations with file name, page number, and chunk ID.

Strong resume-style explanation: "Implemented grounded LLM answer generation using retrieved healthcare document chunks, with structured source citations for traceability."

### Why Did You Choose This Tool Questions

Question: Why use `gpt-4o-mini`?

Short answer: It is a practical default for cost-effective answer generation.

Detailed answer: It is suitable for development because it is cheaper and fast enough for many RAG workflows. The model is configurable through settings.

### Limitations Questions

Question: What are the limitations of Version 7?

Short answer: It is command-line only and has not been evaluated yet.

Detailed answer: It does not expose an API, does not have a UI, does not include RAGAS evaluation, does not handle OCR, and has not been tested with real healthcare PDFs and real OpenAI calls yet.

### Production Improvement Questions

Question: How would you improve answer generation in production?

Short answer: Add evaluation, stricter citation checks, prompt versioning, logging, and safety filters.

Detailed answer: I would add RAGAS evaluation, citation validation, retrieval quality monitoring, prompt templates with version control, refusal rules for insufficient context, audit logs, and human review for high-risk healthcare use cases.

## Version 8: FastAPI Backend

### 1. What I Built

I added a FastAPI backend.

Version 8 includes:
- `backend/app/main.py`
- `backend/app/api/routes.py`
- `backend/app/models/api.py`
- `backend/app/rag/pipeline.py`
- `scripts/run_api.py`
- `tests/test_api.py`
- app version `0.8.0`

The project can now expose the RAG pipeline through HTTP endpoints.

### 2. Why I Built It

Command-line scripts are useful for learning, but real applications usually need an API.

FastAPI lets other systems call the backend over HTTP. Later, the Streamlit frontend will call this API.

### 3. What Each File Does

`backend/app/main.py`

This creates the FastAPI application.

`backend/app/api/routes.py`

This defines the API endpoints:
- `GET /health`
- `POST /ask`

`backend/app/models/api.py`

This defines API request and response schemas using Pydantic.

`backend/app/rag/pipeline.py`

This orchestrates the RAG flow:

```text
question -> retrieval -> grounded answer
```

`scripts/run_api.py`

This starts the local FastAPI server with Uvicorn.

`tests/test_api.py`

This tests the API endpoints. The `/ask` test mocks the RAG pipeline so tests do not call OpenAI.

### 4. How The Code Works In Simple Words

The API has two main endpoints.

`GET /health`

This checks whether the backend is alive.

`POST /ask`

This receives a question like:

```json
{
  "question": "What does the document say about diabetes?"
}
```

Then it calls the RAG pipeline and returns:

```json
{
  "answer": "...",
  "citations": [...]
}
```

### 5. How This Step Connects To The Full RAG Pipeline

The RAG pipeline now has an API layer:

```text
client
-> FastAPI /ask
-> semantic retrieval
-> grounded answer generation
-> citations
-> API response
```

This is the backend interface that the future Streamlit frontend will use.

### 6. How This Step Connects To The Resume

This version supports the FastAPI backend part of the resume stack.

A clear way to describe this version is:

"I exposed the RAG pipeline through a FastAPI backend with health and question-answering endpoints, typed request/response schemas, and API tests."

### 7. What Changed From Version 7

Version 7 generated answers through command-line scripts.

Version 8 exposes the backend through HTTP.

New behavior:
- FastAPI app entrypoint
- `/health` endpoint
- `/ask` endpoint
- Pydantic API schemas
- API tests
- Uvicorn runner script

### 8. What Output I Should Expect

Running:

```bash
python3 scripts/run_api.py
```

starts the API server.

Then this URL should work:

```text
http://127.0.0.1:8000/health
```

FastAPI docs should be available at:

```text
http://127.0.0.1:8000/docs
```

Running tests:

```bash
python3 -m unittest discover -s tests
```

should show:

```text
Ran 26 tests
OK
```

### 9. Common Mistakes And How To Fix Them

Mistake: Expecting `/ask` to work without real vectors and an API key.

Fix: Add PDFs, build the vector store, and use a local `.env` with `OPENAI_API_KEY`.

Mistake: Confusing `/health` with full RAG validation.

Fix: `/health` only checks that the backend is running.

Mistake: Forgetting the server is a long-running process.

Fix: Stop it with `Ctrl+C` in the terminal.

Mistake: Calling the wrong URL.

Fix: Use `http://127.0.0.1:8000/health` or `http://127.0.0.1:8000/docs`.

### 10. What I Will Build Next

In Version 9, I will add a Streamlit frontend.

That means a user will be able to type questions into a simple web interface instead of calling the API manually.

## Version 8 ChatGPT Summary

We completed Version 8 of the Enterprise Healthcare Document Intelligence RAG Platform. Version 8 added a FastAPI backend. It did not implement Streamlit, Unstructured, OCR, Docker, AWS, or RAGAS yet.

Files added include `backend/app/main.py`, `backend/app/api/routes.py`, `backend/app/models/api.py`, `backend/app/rag/pipeline.py`, `scripts/run_api.py`, and `tests/test_api.py`. The API includes `GET /health` for backend status and `POST /ask` for question answering through the RAG pipeline. API request and response schemas are defined with Pydantic. The `/ask` tests mock the RAG pipeline so they do not call OpenAI or require a real API key.

The app version was updated to `0.8.0`. Tests were verified with `python3 -m unittest discover -s tests`, which ran 26 tests successfully. A Python syntax check was also verified for the FastAPI files.

## Version 8 Interview Preparation

### Most Likely Interview Questions

Question: What did you build in Version 8?

Short answer: I built the FastAPI backend for the RAG platform.

Detailed answer: I exposed the RAG pipeline through HTTP endpoints, added typed request and response schemas, and tested the API without calling OpenAI.

Follow-up: What endpoints did you create?

Answer: `GET /health` for backend health and `POST /ask` for question answering.

What not to say: "FastAPI automatically makes the RAG system production-ready."

Red flag to avoid: Ignoring authentication, logging, validation, and deployment concerns.

### Theory Questions

Question: What is FastAPI?

Short answer: FastAPI is a Python framework for building APIs.

Detailed answer: It lets me define HTTP endpoints, validate request bodies with Pydantic, and return structured JSON responses.

Question: Why use an API layer?

Short answer: It lets other applications call the RAG system.

Detailed answer: The frontend, external tools, or deployment environment can interact with the backend through HTTP instead of running Python scripts directly.

### Coding Questions

Question: What does `backend/app/main.py` do?

Short answer: It creates the FastAPI app.

Detailed answer: It loads settings, creates a FastAPI instance, and includes the API router.

Question: What does `backend/app/rag/pipeline.py` do?

Short answer: It orchestrates retrieval and answer generation.

Detailed answer: It creates embeddings and an LLM client, retrieves relevant chunks from ChromaDB, and generates a grounded answer.

### Tricky Questions

Question: Why mock the RAG pipeline in API tests?

Short answer: To test API behavior without external dependencies.

Detailed answer: API tests should verify routing, validation, response shape, and error handling. Mocking avoids OpenAI calls, vector database state, cost, and network failures.

Question: Does `/health` prove the whole RAG pipeline works?

Short answer: No.

Detailed answer: `/health` only proves the backend is running and can load basic status. Full RAG validation needs integration tests with documents and vectors.

### System Design Questions

Question: Where does FastAPI fit in the architecture?

Short answer: It is the backend interface.

Detailed answer: Users or frontend clients send questions to FastAPI. FastAPI calls the RAG pipeline and returns answers plus citations as JSON.

### Resume Defense Questions

Question: Your resume mentions FastAPI. What did you implement?

Short answer: I implemented a FastAPI backend with health and question-answering endpoints.

Detailed answer: The backend exposes the RAG pipeline through typed HTTP endpoints and includes tests for successful responses, validation, and error handling.

Strong resume-style explanation: "Built a FastAPI backend exposing health and RAG question-answering endpoints with Pydantic schemas and API tests."

### Why Did You Choose This Tool Questions

Question: Why FastAPI?

Short answer: It is fast, modern, and has strong typing support.

Detailed answer: FastAPI works well with Pydantic models, provides automatic OpenAPI docs, and is commonly used for ML and AI service backends.

### Limitations Questions

Question: What are the limitations of Version 8?

Short answer: It has no UI, auth, Docker, or cloud deployment yet.

Detailed answer: It does not include Streamlit, authentication, rate limits, logging, Docker, AWS deployment, OCR, Unstructured parsing, or RAGAS evaluation yet.

### Production Improvement Questions

Question: How would you improve this API for production?

Short answer: Add authentication, logging, rate limits, error handling, monitoring, and deployment automation.

Detailed answer: I would add request IDs, structured logs, auth, CORS policy, rate limiting, streaming responses, async job handling for ingestion, Docker health checks, CI/CD, and cloud deployment on AWS.

## Version 9: Streamlit Frontend

### 1. What I Built

I added a Streamlit frontend.

Version 9 includes:
- `frontend/app.py`
- `frontend/api_client.py`
- `frontend/__init__.py`
- `scripts/run_frontend.py`
- `tests/test_frontend_api_client.py`
- app version `0.9.0`

The project now has a simple user interface for asking questions and viewing answers with citations.

### 2. Why I Built It

An API is useful for developers, but a frontend is easier for users.

Streamlit lets me build a lightweight UI quickly so a user can type a question, send it to FastAPI, and see the answer and citations.

### 3. What Each File Does

`frontend/app.py`

This is the Streamlit UI.

It has:
- backend URL input
- question text box
- ask button
- answer display
- citations display
- error messages

`frontend/api_client.py`

This calls the FastAPI backend from the frontend.

It sends requests to:

```text
POST /ask
```

`scripts/run_frontend.py`

This starts the Streamlit app.

`tests/test_frontend_api_client.py`

This tests frontend backend-call behavior with mocked HTTP responses.

### 4. How The Code Works In Simple Words

The user opens Streamlit.

The user types a question.

Streamlit sends that question to FastAPI:

```text
Streamlit -> FastAPI /ask
```

FastAPI runs the RAG pipeline and returns:
- answer
- citations

Streamlit displays both.

### 5. How This Step Connects To The Full RAG Pipeline

The project now has a user-facing layer:

```text
User
-> Streamlit frontend
-> FastAPI backend
-> retrieval
-> grounded answer
-> citations
-> Streamlit display
```

### 6. How This Step Connects To The Resume

This version supports the Streamlit frontend part of the resume stack.

A clear way to describe this version is:

"I built a Streamlit frontend that connects to the FastAPI RAG backend, allowing users to submit questions and view grounded answers with source citations."

### 7. What Changed From Version 8

Version 8 exposed the RAG pipeline through FastAPI.

Version 9 adds a frontend UI.

New behavior:
- user can type questions in a web interface
- frontend calls backend `/ask`
- answer is displayed on screen
- citations are displayed under the answer
- frontend handles backend connection errors

### 8. What Output I Should Expect

Start FastAPI:

```bash
python3 scripts/run_api.py
```

Start Streamlit in a second terminal:

```bash
python3 scripts/run_frontend.py
```

Open:

```text
http://localhost:8501
```

Running tests:

```bash
python3 -m unittest discover -s tests
```

should show:

```text
Ran 30 tests
OK
```

### 9. Common Mistakes And How To Fix Them

Mistake: Running Streamlit without FastAPI.

Fix: Start FastAPI first with `python3 scripts/run_api.py`.

Mistake: Expecting real answers without embeddings.

Fix: Real answers require PDFs, a local API key, and a built ChromaDB vector store.

Mistake: Calling the wrong backend URL.

Fix: Use `http://127.0.0.1:8000` in the Streamlit sidebar.

Mistake: Thinking Streamlit replaces FastAPI.

Fix: Streamlit is the frontend. FastAPI is the backend.

### 10. What I Will Build Next

In Version 10, I will add Unstructured parsing.

That will improve document ingestion for more complex PDFs.

## Version 9 ChatGPT Summary

We completed Version 9 of the Enterprise Healthcare Document Intelligence RAG Platform. Version 9 added a Streamlit frontend. It did not implement Unstructured parsing, OCR, Docker, AWS, or RAGAS yet.

Files added include `frontend/app.py`, `frontend/api_client.py`, `frontend/__init__.py`, `scripts/run_frontend.py`, and `tests/test_frontend_api_client.py`. The Streamlit app provides a question input, backend URL setting, answer display, citation display, and error handling. The frontend API client calls the FastAPI `/ask` endpoint. Tests mock backend HTTP responses, so they do not call OpenAI or require the FastAPI server.

The app version was updated to `0.9.0`. Tests were verified with `python3 -m unittest discover -s tests`, which ran 30 tests successfully. The Streamlit app was also started locally and booted successfully at `http://localhost:8501`.

## Version 9 Interview Preparation

### Most Likely Interview Questions

Question: What did you build in Version 9?

Short answer: I built the Streamlit frontend.

Detailed answer: I added a user interface where users can type questions, send them to the FastAPI backend, and view answers with source citations.

Follow-up: Why use Streamlit?

Answer: Streamlit is fast for building Python-based ML and GenAI prototypes with simple UI needs.

What not to say: "Streamlit is the backend."

Red flag to avoid: Confusing frontend and backend responsibilities.

### Theory Questions

Question: What is a frontend?

Short answer: It is the user-facing part of the application.

Detailed answer: The frontend lets users interact with the system visually instead of calling APIs or scripts manually.

Question: Why separate frontend and backend?

Short answer: They do different jobs.

Detailed answer: The frontend handles user interaction. The backend handles API requests, retrieval, LLM calls, and data processing.

### Coding Questions

Question: What does `frontend/api_client.py` do?

Short answer: It calls the FastAPI backend.

Detailed answer: It sends a POST request to `/ask` with the user's question and returns the backend JSON response.

Question: What does `frontend/app.py` do?

Short answer: It defines the Streamlit UI.

Detailed answer: It creates the question box, backend URL input, submit button, answer display, citations display, and error handling.

### Tricky Questions

Question: Can Streamlit answer questions by itself?

Short answer: No.

Detailed answer: Streamlit only displays the UI. It sends questions to FastAPI, and FastAPI runs the RAG pipeline.

Question: What happens if FastAPI is not running?

Short answer: The frontend shows a connection error.

Detailed answer: The API client catches request errors and displays a clear message telling the user to start the backend.

### System Design Questions

Question: Where does Streamlit fit in the architecture?

Short answer: It is the presentation layer.

Detailed answer: Users interact with Streamlit, Streamlit calls FastAPI, and FastAPI runs retrieval and answer generation.

### Resume Defense Questions

Question: Your resume mentions Streamlit. What did you implement?

Short answer: I implemented a Streamlit frontend for the healthcare RAG backend.

Detailed answer: The frontend connects to FastAPI, submits user questions, and displays grounded answers with citations.

Strong resume-style explanation: "Built a Streamlit frontend connected to a FastAPI RAG backend for question answering over healthcare documents with citation display."

### Why Did You Choose This Tool Questions

Question: Why Streamlit instead of React?

Short answer: Streamlit is faster for a Python-first AI prototype.

Detailed answer: For GenAI demos and internal tools, Streamlit lets me build a usable UI quickly without adding a separate JavaScript stack.

### Limitations Questions

Question: What are the limitations of Version 9?

Short answer: It is a simple UI and not production hardened.

Detailed answer: It does not include authentication, user management, upload flows, streaming responses, advanced styling, or deployment.

### Production Improvement Questions

Question: How would you improve the frontend in production?

Short answer: Add authentication, upload support, streaming, better error states, and user feedback.

Detailed answer: I would add login, document upload, answer streaming, loading states, request history, feedback buttons, role-based access, and deployment behind HTTPS.

## Version 10: Unstructured PDF Parsing

### 1. What I Built

I added an Unstructured-based PDF parsing path.

Version 10 includes:
- `backend/app/ingestion/unstructured_loader.py`
- `scripts/ingest_unstructured_pdfs.py`
- `tests/test_unstructured_loader.py`
- app version `0.10.0`

The project now has two ingestion approaches:
- PyPDF for basic text-based PDF extraction
- Unstructured for more advanced document parsing

### 2. Why I Built It

PyPDF is a good baseline parser, but real healthcare PDFs can have complex layouts.

Unstructured is useful because it can split documents into layout-aware elements such as titles, paragraphs, tables, and other document components.

### 3. What Each File Does

`backend/app/ingestion/unstructured_loader.py`

This contains Unstructured parsing logic.

It has:
- `load_pdf_pages_with_unstructured`
- `load_pdfs_from_directory_with_unstructured`
- `UnstructuredParserUnavailableError`

`load_pdf_pages_with_unstructured`

This parses one PDF with Unstructured and groups extracted elements by page number.

`load_pdfs_from_directory_with_unstructured`

This parses every PDF in a directory using Unstructured.

`UnstructuredParserUnavailableError`

This gives a clear error if local optional PDF parsing dependencies are missing.

`scripts/ingest_unstructured_pdfs.py`

This runs Unstructured parsing from the terminal.

`tests/test_unstructured_loader.py`

This tests Unstructured parsing behavior using fake Unstructured elements, so tests do not depend on a real complex PDF.

### 4. How The Code Works In Simple Words

Unstructured returns document elements.

An element might represent a paragraph, heading, list item, or other document piece.

The code reads each element, checks its page number, and groups all text from the same page together.

Then it returns the same `ParsedPDFPage` format used by PyPDF.

That means downstream code can keep using the same pipeline:

```text
ParsedPDFPage -> LangChain Document -> chunks -> embeddings -> ChromaDB
```

### 5. How This Step Connects To The Full RAG Pipeline

The ingestion layer is now stronger:

```text
PDF
-> PyPDF parser OR Unstructured parser
-> ParsedPDFPage objects
-> LangChain documents
-> chunks
-> embeddings
-> retrieval
-> answer
```

Unstructured improves the document parsing stage before chunking and retrieval.

### 6. How This Step Connects To The Resume

This version supports the Unstructured part of the resume stack.

A clear way to describe this version is:

"I added an Unstructured-based PDF parser path that extracts layout-aware document elements and converts them into the same page-level format used by the RAG pipeline."

### 7. What Changed From Version 9

Version 9 added the Streamlit frontend.

Version 10 improves document ingestion.

New behavior:
- Unstructured parser module
- Unstructured ingestion script
- clear optional dependency error
- tests for grouping Unstructured elements by page

### 8. What Output I Should Expect

Running:

```bash
python3 scripts/ingest_unstructured_pdfs.py
```

with an empty `data/raw/` folder prints:

```text
PDF pages parsed with Unstructured: 0
```

That is correct.

Running tests:

```bash
python3 -m unittest discover -s tests
```

should show:

```text
Ran 34 tests
OK
```

### 9. Common Mistakes And How To Fix Them

Mistake: Expecting Unstructured to work the same on every Mac immediately.

Fix: Some PDF features require optional system dependencies. The code now reports a clear setup message if those are missing.

Mistake: Thinking Unstructured replaces PyPDF.

Fix: It does not have to replace PyPDF. In production, both can be used as parser options.

Mistake: Thinking Unstructured is OCR.

Fix: Unstructured helps parse document structure. OCR for scanned PDFs comes in the next version.

Mistake: Expecting real parsing when `data/raw/` is empty.

Fix: Add PDFs to `data/raw/`.

### 10. What I Will Build Next

In Version 11, I will add OCR fallback for scanned PDFs.

That means if a PDF page has no extractable text, the system will have a path to extract text from page images.

## Version 10 ChatGPT Summary

We completed Version 10 of the Enterprise Healthcare Document Intelligence RAG Platform. Version 10 added an Unstructured-based PDF parsing path. It did not implement OCR fallback, RAGAS, Docker, AWS S3, or AWS EC2 yet.

Files added include `backend/app/ingestion/unstructured_loader.py`, `scripts/ingest_unstructured_pdfs.py`, and `tests/test_unstructured_loader.py`. The Unstructured loader parses PDF elements, groups text by page number, and returns the same `ParsedPDFPage` format used by the rest of the pipeline. The script runs Unstructured parsing from the terminal. Tests use fake Unstructured elements, so they do not require a real complex PDF.

The app version was updated to `0.10.0`. The project now has both PyPDF and Unstructured ingestion paths. Tests were verified with `python3 -m unittest discover -s tests`, which ran 34 tests successfully. The Unstructured ingestion script was verified with an empty `data/raw/` folder and correctly reported 0 parsed pages.

## Version 10 Interview Preparation

### Most Likely Interview Questions

Question: What did you build in Version 10?

Short answer: I added an Unstructured PDF parser path.

Detailed answer: I implemented a parser that uses Unstructured to extract document elements from PDFs, groups those elements by page number, and converts them into the same page-level format used by the RAG pipeline.

Follow-up: Why add Unstructured if you already have PyPDF?

Answer: PyPDF is a simple text extractor. Unstructured can better handle complex document layouts and element-level parsing.

What not to say: "Unstructured solves every PDF problem."

Red flag to avoid: Confusing Unstructured with OCR.

### Theory Questions

Question: What is Unstructured?

Short answer: It is a library for parsing unstructured documents into useful elements.

Detailed answer: It can break documents into components such as titles, paragraphs, and tables, which can be useful before chunking and retrieval.

Question: Why do healthcare PDFs need advanced parsing?

Short answer: They can have complex layouts.

Detailed answer: Healthcare documents may include headings, tables, forms, discharge instructions, lab results, and multi-column layouts. Better parsing can improve retrieval quality.

### Coding Questions

Question: What does `load_pdf_pages_with_unstructured` do?

Short answer: It parses one PDF with Unstructured and returns page-level text objects.

Detailed answer: It calls Unstructured's PDF partitioner, reads each element's text and page number, groups elements by page, and returns `ParsedPDFPage` objects.

Question: Why return `ParsedPDFPage` instead of a new object?

Short answer: To keep the downstream pipeline consistent.

Detailed answer: PyPDF and Unstructured can both feed the same LangChain document conversion and chunking logic.

### Tricky Questions

Question: Is Unstructured OCR?

Short answer: No, not by itself in this project version.

Detailed answer: Unstructured helps parse document elements. OCR specifically extracts text from images or scanned pages, and that comes next.

Question: Why do tests use fake Unstructured elements?

Short answer: To test our logic without relying on external PDF dependencies.

Detailed answer: Unit tests should verify grouping and metadata behavior. Real PDF parsing can be covered by integration tests later.

### System Design Questions

Question: Where does Unstructured fit in the architecture?

Short answer: In the ingestion layer.

Detailed answer: It is an alternative parser before LangChain documents, chunking, embeddings, retrieval, and answer generation.

### Resume Defense Questions

Question: Your resume mentions Unstructured. What did you implement?

Short answer: I added an Unstructured parser path for PDF ingestion.

Detailed answer: The code can parse Unstructured elements, preserve page metadata, and pass the result into the existing RAG pipeline format.

Strong resume-style explanation: "Added an Unstructured-based PDF parsing path for complex healthcare documents, normalizing extracted elements into page-level RAG inputs."

### Why Did You Choose This Tool Questions

Question: Why use Unstructured?

Short answer: It is useful for complex document parsing.

Detailed answer: It can extract structured elements from messy files, which can improve chunk quality and retrieval performance.

### Limitations Questions

Question: What are the limitations of Version 10?

Short answer: OCR fallback is not implemented yet.

Detailed answer: Unstructured parsing is added, but scanned PDFs still need OCR. Some Unstructured PDF features also require extra system dependencies.

### Production Improvement Questions

Question: How would you improve parsing in production?

Short answer: Add parser routing, OCR fallback, document quality checks, and integration tests.

Detailed answer: I would automatically choose PyPDF, Unstructured, or OCR based on document type and text quality, then log parser results and evaluate retrieval quality.

## Version 11: OCR Fallback For Scanned PDFs

### 1. What I Built

I added OCR fallback for scanned PDFs.

Version 11 includes:
- `backend/app/ingestion/ocr_loader.py`
- `scripts/ingest_ocr_pdfs.py`
- `tests/test_ocr_loader.py`
- app version `0.11.0`

The project now has a path for PDFs where normal text extraction fails.

### 2. Why I Built It

Some PDFs are not real text PDFs.

They are scanned images inside a PDF file.

PyPDF may return empty text for those pages. OCR solves this by converting the page image into text.

### 3. What Each File Does

`backend/app/ingestion/ocr_loader.py`

This contains OCR fallback logic.

It has:
- `load_pdf_pages_with_ocr`
- `load_pdf_pages_with_ocr_fallback`
- `load_pdfs_from_directory_with_ocr_fallback`
- `OCRUnavailableError`

`load_pdf_pages_with_ocr`

This converts PDF pages into images and extracts text from each image using OCR.

`load_pdf_pages_with_ocr_fallback`

This tries PyPDF first. If a page has no extractable text, it uses OCR for that page.

`load_pdfs_from_directory_with_ocr_fallback`

This applies OCR fallback to every PDF in a directory.

`OCRUnavailableError`

This gives clear messages when OCR dependencies are missing.

`scripts/ingest_ocr_pdfs.py`

This runs OCR fallback ingestion from the terminal.

`tests/test_ocr_loader.py`

This tests OCR behavior with fake page images, so tests do not require Tesseract or Poppler.

### 4. How The Code Works In Simple Words

The fallback flow is:

```text
Try PyPDF first
-> if page text exists, keep it
-> if page text is empty, use OCR
```

OCR flow:

```text
PDF page
-> image
-> Tesseract OCR
-> text
```

The result is still returned as `ParsedPDFPage`, so downstream RAG code stays the same.

### 5. How This Step Connects To The Full RAG Pipeline

The ingestion layer now handles three paths:

```text
PyPDF
Unstructured
OCR fallback
```

All paths normalize into:

```text
ParsedPDFPage
-> LangChain Document
-> chunks
-> embeddings
-> ChromaDB
-> retrieval
-> answer
```

### 6. How This Step Connects To The Resume

This version supports the OCR fallback part of the resume stack.

A clear way to describe this version is:

"I implemented OCR fallback for scanned PDFs by converting pages to images and extracting text with Tesseract-style OCR, while preserving page-level metadata for downstream citations."

### 7. What Changed From Version 10

Version 10 added Unstructured parsing.

Version 11 adds OCR fallback.

New behavior:
- detects pages with empty PyPDF text
- runs OCR for those pages
- merges OCR text with PyPDF text
- preserves file name and page number metadata
- handles missing OCR dependencies clearly

### 8. What Output I Should Expect

Running:

```bash
python3 scripts/ingest_ocr_pdfs.py
```

with an empty `data/raw/` folder prints:

```text
PDF pages parsed with OCR fallback: 0
```

That is correct.

Running tests:

```bash
python3 -m unittest discover -s tests
```

should show:

```text
Ran 39 tests
OK
```

### 9. Common Mistakes And How To Fix Them

Mistake: Thinking installing `pytesseract` is enough.

Fix: `pytesseract` is only the Python wrapper. The Tesseract system tool must also be installed for real OCR.

Mistake: Thinking installing `pdf2image` is enough.

Fix: `pdf2image` needs Poppler installed locally to convert PDF pages into images.

Mistake: Running OCR on every PDF.

Fix: Use OCR as fallback because it is slower and more expensive computationally than text extraction.

Mistake: Expecting perfect OCR.

Fix: OCR can make mistakes, especially on low-quality scans, handwriting, tables, and small fonts.

### 10. What I Will Build Next

In Version 12, I will add RAGAS evaluation.

That will help measure answer quality, faithfulness, and retrieval performance.

## Version 11 ChatGPT Summary

We completed Version 11 of the Enterprise Healthcare Document Intelligence RAG Platform. Version 11 added OCR fallback for scanned PDFs. It did not implement RAGAS, Docker, AWS S3, or AWS EC2 yet.

Files added include `backend/app/ingestion/ocr_loader.py`, `scripts/ingest_ocr_pdfs.py`, and `tests/test_ocr_loader.py`. The OCR loader can convert PDF pages into images and extract text using OCR. It also includes a fallback function that tries PyPDF first and only uses OCR for pages where PyPDF returns no text. OCR output is normalized into the same `ParsedPDFPage` format used by the rest of the RAG pipeline.

The app version was updated to `0.11.0`. Tests were verified with `python3 -m unittest discover -s tests`, which ran 39 tests successfully. The OCR ingestion script was verified with an empty `data/raw/` folder and correctly reported 0 parsed pages. Real OCR requires Python packages plus system tools such as Poppler and Tesseract.

## Version 11 Interview Preparation

### Most Likely Interview Questions

Question: What did you build in Version 11?

Short answer: I added OCR fallback for scanned PDFs.

Detailed answer: I implemented an OCR path that converts PDF pages into images, extracts text from those images, and preserves page-level metadata for downstream RAG citations.

Follow-up: Why do you need OCR?

Answer: Some PDFs are scanned images with no embedded text. PyPDF cannot extract text from those pages, so OCR is needed.

What not to say: "OCR is always accurate."

Red flag to avoid: Ignoring OCR quality problems.

### Theory Questions

Question: What is OCR?

Short answer: OCR means Optical Character Recognition.

Detailed answer: OCR extracts text from images, such as scanned PDF pages or photographed documents.

Question: Why is OCR important in healthcare?

Short answer: Many healthcare documents are scanned.

Detailed answer: Medical records, forms, discharge papers, and faxes may be image-based. OCR makes those documents searchable.

### Coding Questions

Question: What does `load_pdf_pages_with_ocr_fallback` do?

Short answer: It uses PyPDF first and OCR only when needed.

Detailed answer: It reads PDF pages with PyPDF. Pages with text are kept. Pages without text are replaced with OCR-extracted text.

Question: Why return `ParsedPDFPage`?

Short answer: To keep the downstream pipeline consistent.

Detailed answer: PyPDF, Unstructured, and OCR all produce the same page-level format for LangChain conversion and chunking.

### Tricky Questions

Question: Is `pytesseract` enough for OCR?

Short answer: No.

Detailed answer: `pytesseract` is a Python wrapper. The Tesseract system binary must also be installed.

Question: Is `pdf2image` enough to convert PDFs?

Short answer: No.

Detailed answer: `pdf2image` usually needs Poppler installed on the machine.

### System Design Questions

Question: Where does OCR fit in the architecture?

Short answer: In the ingestion layer as a fallback.

Detailed answer: OCR runs when normal PDF text extraction fails, then the extracted text flows into LangChain documents, chunks, embeddings, retrieval, and answer generation.

### Resume Defense Questions

Question: Your resume mentions OCR fallback. What did you implement?

Short answer: I implemented a fallback path for scanned PDF pages.

Detailed answer: The system can detect pages with no extracted text and use OCR to extract text from page images while preserving source metadata.

Strong resume-style explanation: "Implemented OCR fallback for scanned healthcare PDFs, normalizing extracted image text into page-level RAG inputs with citation metadata."

### Why Did You Choose This Tool Questions

Question: Why use Tesseract-style OCR?

Short answer: It is a common open-source OCR approach.

Detailed answer: Tesseract is widely used, works locally, and is a reasonable baseline before considering cloud OCR services.

### Limitations Questions

Question: What are the limitations of Version 11?

Short answer: OCR is implemented as a fallback but not production tuned.

Detailed answer: It does not include image preprocessing, confidence scoring, OCR quality evaluation, table extraction, handwriting handling, or cloud OCR comparison.

### Production Improvement Questions

Question: How would you improve OCR in production?

Short answer: Add preprocessing, confidence scores, quality checks, and cloud OCR options.

Detailed answer: I would add deskewing, denoising, page rotation detection, confidence thresholds, manual review workflows, OCR result caching, and compare Tesseract with AWS Textract for complex healthcare forms.

## Version 12: RAGAS Evaluation

### 1. What I Built

I added a RAGAS evaluation layer.

Version 12 includes:
- `evaluation/__init__.py`
- `evaluation/ragas_evaluator.py`
- `scripts/run_ragas_evaluation.py`
- `tests/test_ragas_evaluator.py`
- app version `0.12.0`

The project now has a way to prepare evaluation examples in the format RAGAS expects.

### 2. Why I Built It

RAG systems need evaluation.

It is not enough to say the system returns answers. I need a way to measure whether answers are grounded, relevant, and supported by retrieved context.

RAGAS helps evaluate RAG quality.

### 3. What Each File Does

`evaluation/ragas_evaluator.py`

This contains evaluation helper code.

It has:
- `RAGASEvaluationExample`
- `build_evaluation_dataset`
- `sample_evaluation_examples`
- `run_ragas_evaluation`

`RAGASEvaluationExample`

This stores one evaluation row:
- question
- answer
- contexts
- ground truth

`build_evaluation_dataset`

This converts evaluation examples into a Hugging Face `Dataset`, which RAGAS can evaluate.

`sample_evaluation_examples`

This provides a tiny local example dataset for learning.

`run_ragas_evaluation`

This runs RAGAS metrics such as faithfulness, answer relevancy, and context precision.

`scripts/run_ragas_evaluation.py`

This runs a dry run by default. With `--run`, it attempts real RAGAS evaluation.

`tests/test_ragas_evaluator.py`

This tests the evaluation dataset creation locally without calling OpenAI.

### 4. How The Code Works In Simple Words

RAGAS expects data shaped like this:

```text
question
answer
contexts
ground_truth
```

The code creates examples in that shape.

Then it converts them into a dataset.

The dry-run script shows:
- how many examples exist
- which columns exist
- whether the dataset is ready

Real RAGAS evaluation can be run later when local API keys are configured.

### 5. How This Step Connects To The Full RAG Pipeline

The system can now be evaluated:

```text
question
-> retrieved contexts
-> generated answer
-> ground truth
-> RAGAS metrics
```

This helps measure whether the RAG pipeline is actually working well.

### 6. How This Step Connects To The Resume

This version supports the RAGAS evaluation part of the resume stack.

A clear way to describe this version is:

"I added a RAGAS evaluation layer that prepares question, answer, context, and ground-truth examples for measuring RAG faithfulness, relevancy, and retrieval quality."

### 7. What Changed From Version 11

Version 11 added OCR fallback.

Version 12 adds evaluation.

New behavior:
- evaluation example format
- Hugging Face Dataset creation
- RAGAS evaluator function
- dry-run evaluation script
- tests for evaluation data shape

### 8. What Output I Should Expect

Running:

```bash
python3 scripts/run_ragas_evaluation.py
```

prints:

```text
Evaluation examples: 2
Dataset columns: question, answer, contexts, ground_truth
Dry run only...
```

Running tests:

```bash
python3 -m unittest discover -s tests
```

should show:

```text
Ran 42 tests
OK
```

### 9. Common Mistakes And How To Fix Them

Mistake: Thinking dry run means real evaluation happened.

Fix: Dry run only validates dataset shape. Real evaluation uses `--run`.

Mistake: Running real RAGAS evaluation without API keys.

Fix: Add local API keys in `.env` before running real metrics.

Mistake: Evaluating only one example and trusting the result.

Fix: Use a larger, representative evaluation set.

Mistake: Treating RAGAS as the only evaluation needed.

Fix: Combine RAGAS with human review, domain checks, and retrieval debugging.

### 10. What I Will Build Next

In Version 13, I will add Docker setup.

That means the app can be packaged and run in containers.

## Version 12 ChatGPT Summary

We completed Version 12 of the Enterprise Healthcare Document Intelligence RAG Platform. Version 12 added RAGAS evaluation support. It did not implement Docker, AWS S3, or AWS EC2 yet.

Files added include `evaluation/__init__.py`, `evaluation/ragas_evaluator.py`, `scripts/run_ragas_evaluation.py`, and `tests/test_ragas_evaluator.py`. The evaluator defines a `RAGASEvaluationExample` structure with question, answer, contexts, and ground truth. It can build a Hugging Face Dataset in the format expected by RAGAS and includes a function for running RAGAS metrics such as faithfulness, answer relevancy, and context precision.

The app version was updated to `0.12.0`. The evaluation script runs in dry-run mode by default so it does not call OpenAI. Tests were verified with `python3 -m unittest discover -s tests`, which ran 42 tests successfully. The dry-run script was verified with `python3 scripts/run_ragas_evaluation.py`.

## Version 12 Interview Preparation

### Most Likely Interview Questions

Question: What did you build in Version 12?

Short answer: I added RAGAS evaluation support.

Detailed answer: I added an evaluation layer that formats RAG examples into question, answer, context, and ground-truth fields so RAGAS can evaluate quality metrics.

Follow-up: Did you run real RAGAS evaluation?

Answer: I added the evaluator and dry-run dataset validation. Real RAGAS evaluation can be run with local API keys using the `--run` flag.

What not to say: "RAGAS proves the system is perfect."

Red flag to avoid: Treating one metric as the whole evaluation strategy.

### Theory Questions

Question: What is RAGAS?

Short answer: RAGAS is a framework for evaluating RAG systems.

Detailed answer: It can measure qualities like faithfulness, answer relevancy, and context precision using questions, answers, retrieved contexts, and ground truth.

Question: Why evaluate RAG?

Short answer: RAG systems can retrieve wrong context or generate unsupported answers.

Detailed answer: Evaluation helps identify hallucinations, irrelevant retrieval, poor context quality, and answer quality problems.

### Coding Questions

Question: What does `build_evaluation_dataset` do?

Short answer: It builds a dataset in the format RAGAS expects.

Detailed answer: It takes evaluation examples and creates columns for question, answer, contexts, and ground truth.

Question: Why does the script dry-run by default?

Short answer: To avoid accidental LLM calls and API cost.

Detailed answer: Real RAGAS evaluation may call an LLM, so dry run lets me verify the dataset first.

### Tricky Questions

Question: Is RAGAS enough for healthcare evaluation?

Short answer: No.

Detailed answer: RAGAS is useful, but healthcare systems also need expert review, safety checks, citation validation, privacy review, and domain-specific evaluation.

Question: What is faithfulness?

Short answer: It measures whether the answer is supported by retrieved context.

Detailed answer: A faithful answer should not add unsupported claims beyond the provided context.

### System Design Questions

Question: Where does evaluation fit in the architecture?

Short answer: After retrieval and answer generation.

Detailed answer: The system produces answers and retrieved contexts, then evaluation checks whether those answers are relevant and grounded.

### Resume Defense Questions

Question: Your resume mentions RAGAS. What did you implement?

Short answer: I implemented a RAGAS evaluation layer and dataset builder.

Detailed answer: The project can prepare RAGAS-compatible examples and run metrics for faithfulness, answer relevancy, and context precision.

Strong resume-style explanation: "Added a RAGAS evaluation layer to measure faithfulness, answer relevancy, and retrieval quality for healthcare RAG outputs."

### Why Did You Choose This Tool Questions

Question: Why RAGAS?

Short answer: It is designed specifically for RAG evaluation.

Detailed answer: It provides metrics that focus on retrieval context and grounded answer quality, which are central to RAG systems.

### Limitations Questions

Question: What are the limitations of Version 12?

Short answer: It has sample evaluation data, not a full production benchmark.

Detailed answer: It does not yet include a large domain-specific test set, expert-labeled healthcare answers, automated CI evaluation thresholds, or human review workflows.

### Production Improvement Questions

Question: How would you improve evaluation in production?

Short answer: Add a larger benchmark, CI thresholds, human review, and monitoring.

Detailed answer: I would build a representative healthcare evaluation set, add expert-reviewed ground truth, track RAGAS scores over time, fail CI on regressions, and monitor real-world answer feedback.

## Version 13: Docker Setup

### 1. What We Built

Version 13 adds Docker support for the project.

Docker lets the app run inside containers. A container is like a small packaged environment that includes the Python runtime, installed dependencies, and the command needed to start the app.

Version 13 includes:
- `backend/Dockerfile`
- `frontend/Dockerfile`
- `docker-compose.yml`
- `.dockerignore`
- Docker configuration tests
- frontend backend URL configuration through `BACKEND_URL`

Version 13 does not add AWS S3 or AWS EC2 yet. Those are still future versions.

### 2. Why We Built It

Before Docker, the backend and frontend were run directly on the local machine.

That works for learning, but production projects usually need a repeatable way to run the same app on different machines.

Docker helps because:
- the backend can run the same way on a laptop or server
- the frontend can run the same way on a laptop or server
- dependencies are installed inside the image
- Docker Compose can start multiple services together
- this prepares the project for AWS EC2 deployment later

### 3. What Each File Or Folder Does

`backend/Dockerfile`

This describes how to build the backend container image. It uses Python, installs dependencies from `requirements.txt`, copies the backend code, exposes port `8000`, and starts FastAPI with `uvicorn`.

`frontend/Dockerfile`

This describes how to build the frontend container image. It uses Python, installs dependencies, copies the frontend code, exposes port `8501`, and starts Streamlit.

`docker-compose.yml`

This file runs the backend and frontend together.

It defines two services:
- `backend`
- `frontend`

The frontend uses `BACKEND_URL=http://backend:8000` because Docker Compose lets containers talk to each other by service name.

`.dockerignore`

This tells Docker what not to copy into the image.

It excludes secrets, virtual environments, caches, logs, local PDFs, and local ChromaDB files.

This is important because real healthcare documents and API keys should not be baked into Docker images.

`tests/test_docker_config.py`

This checks that the Docker files exist and that Docker Compose defines the expected backend and frontend services.

`frontend/api_client.py`

This now reads `BACKEND_URL` from the environment.

Locally, it defaults to `http://127.0.0.1:8000`.

Inside Docker, Compose sets it to `http://backend:8000`.

### 4. How The Code Works In Simple Words

The backend Dockerfile says:

1. Start from a small Python image.
2. Create `/app` as the working folder.
3. Install Python packages.
4. Copy backend code.
5. Run FastAPI on port `8000`.

The frontend Dockerfile says:

1. Start from a small Python image.
2. Create `/app` as the working folder.
3. Install Python packages.
4. Copy frontend code.
5. Run Streamlit on port `8501`.

Docker Compose says:

1. Build the backend image.
2. Build the frontend image.
3. Run the backend on local port `8000`.
4. Run the frontend on local port `8501`.
5. Let the frontend call the backend using the Docker service name `backend`.

### 5. How This Step Connects To The Full RAG Pipeline

The RAG pipeline already has ingestion, chunking, embeddings, vector storage, retrieval, answer generation, API, UI, OCR, Unstructured parsing, and RAGAS evaluation.

Docker does not change the RAG logic.

Docker packages the application so the backend and frontend can run in a repeatable environment.

In the full pipeline:

PDFs → parsing → chunks → embeddings → ChromaDB → retrieval → LLM answer → citations → FastAPI → Streamlit → Docker container

### 6. How This Step Connects To My Resume

The resume stack includes Docker.

Version 13 honestly supports that resume point because the project now has:
- backend container setup
- frontend container setup
- Docker Compose orchestration
- secret-safe Docker ignore rules
- test coverage for Docker configuration

Strong resume-style explanation:

"Containerized a FastAPI and Streamlit healthcare RAG platform using Docker and Docker Compose, with environment-based configuration and local data volume mounting."

### 7. What Changed From Version 12

Version 12 added RAGAS evaluation.

Version 13 adds containerization.

Before Version 13, the app could run locally with Python commands.

After Version 13, the app can also be built and run with Docker commands.

### 8. What Output I Should Expect

Check Docker Compose configuration:

```bash
docker compose config
```

Expected result: Docker Compose prints the final backend and frontend service configuration.

Build Docker images:

```bash
docker compose build
```

Expected result:

```text
Image rag-healthcare-backend Built
Image rag-healthcare-frontend Built
```

Run containers:

```bash
docker compose up
```

Expected URLs:

```text
http://127.0.0.1:8000/health
http://localhost:8501
```

Run tests:

```bash
python3 -m unittest discover -s tests
```

Expected result: all tests pass.

### 9. Common Mistakes And How To Fix Them

Mistake: Docker command says Docker daemon is not running.

Fix: Open Docker Desktop on Mac and wait until it fully starts.

Mistake: Port `8000` or `8501` is already in use.

Fix: Stop the old local FastAPI or Streamlit process, or change the port mapping in `docker-compose.yml`.

Mistake: Expecting `.env` to be inside the Docker image.

Fix: `.env` should not be copied into images. Docker Compose passes it at runtime if it exists.

Mistake: Expecting real OpenAI calls without an API key.

Fix: Create a local `.env` file on your machine with `OPENAI_API_KEY=...`. Do not paste the key into chat and do not commit `.env`.

Mistake: Expecting local PDFs to be inside GitHub.

Fix: Local PDFs stay in `data/raw/`, which is ignored. Docker Compose mounts `./data` into the backend container for local development.

### 10. What We Will Build Next

In Version 14, I will add the AWS S3 storage path.

That means the project will start preparing for cloud document storage, where PDFs can be uploaded to or referenced from S3 instead of only local `data/raw/`.

## Version 13 ChatGPT Summary

We completed Version 13 of the Enterprise Healthcare Document Intelligence RAG Platform. Version 13 added Docker setup for the existing FastAPI backend and Streamlit frontend. It did not implement AWS S3 or AWS EC2 yet.

Files added include `backend/Dockerfile`, `frontend/Dockerfile`, `docker-compose.yml`, `.dockerignore`, and `tests/test_docker_config.py`. The backend Dockerfile builds a Python image, installs dependencies, copies backend code, exposes port `8000`, and runs FastAPI with `uvicorn`. The frontend Dockerfile builds a Python image, installs dependencies, copies frontend code, exposes port `8501`, and runs Streamlit.

The Docker Compose file defines two services: `backend` and `frontend`. The backend maps port `8000`, loads `.env` at runtime if it exists, and mounts local `data/` into `/app/data`. The frontend maps port `8501`, depends on the backend, and uses `BACKEND_URL=http://backend:8000` so it can call the backend container inside Docker.

The frontend API client was updated to read `BACKEND_URL` from the environment. Locally it still defaults to `http://127.0.0.1:8000`, while Docker Compose sets it to the backend service URL.

The app version was updated to `0.13.0`. Verification included `docker compose config`, `docker compose build`, `python3 scripts/health_check.py`, and `python3 -m unittest discover -s tests`.

Version 13 connects to the resume because it adds real Docker containerization for the healthcare RAG platform. The next version will add the AWS S3 storage path.

## Version 13 Interview Preparation

### Most Likely Interview Questions

Question: What did you build in Version 13?

Short answer: I containerized the FastAPI backend and Streamlit frontend using Docker and Docker Compose.

Detailed answer: I added separate Dockerfiles for the backend and frontend, then added Docker Compose to build and run both services together. The backend runs on port `8000`, the frontend runs on port `8501`, and the frontend talks to the backend through the Docker service name.

Follow-up question: Why separate backend and frontend containers?

Answer: Because they are different services with different startup commands and ports. Keeping them separate is cleaner and closer to production service design.

What not to say: "Docker makes the code faster." Docker mainly improves packaging and environment consistency.

### Theory Questions

Question: What is Docker?

Short answer: Docker packages an application with its runtime environment.

Detailed answer: Docker creates container images. A container runs from an image and includes the app code, dependencies, and startup command, making the app easier to run consistently across machines.

Question: What is Docker Compose?

Short answer: Docker Compose runs multiple containers together.

Detailed answer: Instead of manually starting the backend and frontend separately, Compose defines both services in one YAML file and starts them together.

### Coding Questions

Question: What command starts the backend inside the Docker container?

Short answer: `uvicorn backend.app.main:app --host 0.0.0.0 --port 8000`.

Detailed answer: `uvicorn` starts the FastAPI app. The host is `0.0.0.0` so the app listens inside the container and can be exposed to the host machine.

Question: Why does the frontend use `BACKEND_URL`?

Short answer: So the same code can call different backend URLs in local and Docker environments.

Detailed answer: Locally, the backend is at `http://127.0.0.1:8000`. Inside Docker Compose, the backend is reachable as `http://backend:8000`.

### Tricky Questions

Question: Is `.env` copied into the Docker image?

Short answer: No.

Detailed answer: Secrets should not be baked into images. The `.dockerignore` excludes `.env`, and Compose passes `.env` at runtime if it exists.

Question: Why use `0.0.0.0` instead of `127.0.0.1` inside the container?

Short answer: `0.0.0.0` lets the app receive traffic from outside the container.

Detailed answer: If the app only listens on `127.0.0.1` inside the container, it may only be reachable from inside that container.

### System Design Questions

Question: Where does Docker fit in this RAG architecture?

Short answer: Docker packages the API and UI services.

Detailed answer: The RAG logic stays in the backend. Docker gives the backend and frontend repeatable runtime environments and prepares the project for deployment on EC2.

Question: How would this run in production?

Short answer: Build images, run containers on a server, pass secrets securely, and mount or connect persistent storage.

Detailed answer: On EC2, I would install Docker, pull or build the images, configure environment variables securely, run the services, and use a reverse proxy or load balancer for public traffic.

### Resume Defense Questions

Question: Your resume mentions Docker. What exactly did you do?

Short answer: I created Dockerfiles and a Docker Compose setup for the platform.

Detailed answer: I containerized the FastAPI backend and Streamlit frontend, configured runtime environment variables, exposed the correct ports, mounted local data, and added tests to validate Docker configuration.

Strong resume-style explanation:

"Containerized a healthcare RAG platform with Docker and Docker Compose, separating FastAPI backend and Streamlit frontend services with environment-based configuration."

### Why Did You Choose This Tool Questions

Question: Why Docker?

Short answer: It makes the app easier to run consistently across machines.

Detailed answer: Docker reduces environment mismatch problems. For a production-style project, it also prepares the app for server deployment and CI/CD workflows.

Question: Why Docker Compose?

Short answer: Because this project has more than one service.

Detailed answer: Compose makes it simple to run backend and frontend together and lets the frontend refer to the backend by service name.

### Limitations Questions

Question: What are the limitations of Version 13?

Short answer: It containerizes the app, but it is not a complete cloud deployment yet.

Detailed answer: It does not include AWS S3, EC2 setup, HTTPS, authentication, CI/CD, cloud secrets management, container registry publishing, or production monitoring.

### Production Improvement Questions

Question: How would you improve this in production?

Short answer: Add smaller images, health checks, CI/CD, secret management, and deployment automation.

Detailed answer: I would use slimmer dependency groups, add Docker health checks, use AWS Secrets Manager or SSM Parameter Store, publish images to ECR, deploy on EC2 or ECS, add HTTPS through a reverse proxy or load balancer, and monitor logs and errors.

### Red Flags To Avoid

Do not say:
- "Docker stores my API keys."
- "Docker replaces AWS."
- "Docker means the application is production-ready by itself."
- "The frontend should call `localhost` from inside Docker."

Better answer:

"Docker is the packaging layer. It helps me run the backend and frontend consistently, but production still needs secure secrets, cloud storage, deployment automation, monitoring, and network/security configuration."

## Version 14: AWS S3 Storage Path

### 1. What We Built

Version 14 adds an AWS S3 storage path for healthcare source PDFs.

This means the project now has code that can:
- build a predictable S3 key for a PDF
- create an S3 client
- upload local PDFs to an S3 bucket
- list documents stored under an S3 prefix
- keep AWS configuration in environment variables
- test S3 logic without calling real AWS

Version 14 does not deploy the app to AWS EC2 yet.

### 2. Why We Built It

Until now, documents lived only in the local `data/raw/` folder.

That is fine for local development, but production systems usually store uploaded documents somewhere durable and cloud-based.

AWS S3 is a common choice because it is designed for object storage. In simple words, S3 stores files in buckets. Inside a bucket, each file has a key, which is like the file path.

For this project, S3 prepares the document storage layer before EC2 deployment.

### 3. What Each File Or Folder Does

`backend/app/storage/__init__.py`

This marks `storage` as a Python package.

`backend/app/storage/s3_storage.py`

This contains the S3 helper functions:
- `build_s3_key`
- `create_s3_client`
- `upload_pdf_to_s3`
- `upload_pdfs_to_s3`
- `list_s3_documents`

It also includes an `S3Document` dataclass for document metadata.

`scripts/s3_documents.py`

This is a command-line script for S3 document operations.

It can list S3 documents:

```bash
python3 scripts/s3_documents.py --list
```

It can upload local PDFs:

```bash
python3 scripts/s3_documents.py --upload
```

`tests/test_s3_storage.py`

This tests the S3 logic using fake AWS clients.

The tests do not call real AWS and do not need real AWS credentials.

`backend/app/core/settings.py`

This now includes:
- `aws_region`
- `aws_s3_bucket_name`
- `aws_s3_raw_prefix`

`.env.example`

This now includes safe placeholders for:
- `AWS_REGION`
- `AWS_S3_BUCKET_NAME`
- `AWS_S3_RAW_PREFIX`

`requirements.txt`

This now includes `boto3`, the AWS SDK for Python.

### 4. How The Code Works In Simple Words

`build_s3_key` takes a file name and prefix.

Example:

```text
file name: patient-handbook.pdf
prefix: healthcare-documents/raw
S3 key: healthcare-documents/raw/patient-handbook.pdf
```

`create_s3_client` creates a boto3 S3 client.

It does not hard-code credentials. Real AWS credentials should come from your local AWS setup, environment variables, or an AWS role.

`upload_pdf_to_s3` checks:
- the bucket name exists
- the local file exists
- the file is a PDF

Then it uploads the file to S3.

`list_s3_documents` asks S3 for objects under the configured prefix and returns clean metadata objects.

### 5. How This Step Connects To The Full RAG Pipeline

Before Version 14:

Local PDFs in `data/raw/` were the only document source.

After Version 14:

The project has a cloud storage path.

The pipeline can now be explained like this:

PDFs in S3 or local raw folder -> parsing -> chunks -> embeddings -> ChromaDB -> retrieval -> LLM answer -> citations -> FastAPI -> Streamlit -> Docker -> AWS deployment path

Version 14 does not replace local ingestion yet. It prepares the cloud document storage layer.

### 6. How This Step Connects To My Resume

The resume stack includes AWS S3.

Version 14 honestly supports that because the project now includes:
- S3 settings
- S3 upload path
- S3 listing path
- boto3 dependency
- tests for S3 behavior
- no hard-coded AWS secrets

Strong resume-style explanation:

"Added an AWS S3 document storage layer for healthcare PDFs, including environment-based configuration, upload/list helpers, and mocked tests for cloud storage behavior."

### 7. What Changed From Version 13

Version 13 added Docker.

Version 14 adds AWS S3 document storage support.

Before Version 14, document storage was local-only.

After Version 14, the project has a safe cloud storage path for PDFs.

### 8. What Output I Should Expect

Run tests:

```bash
python3 -m unittest discover -s tests
```

Expected result: all tests pass.

Run the health check:

```bash
python3 scripts/health_check.py
```

Expected result: app version `0.14.0` and status `ok`.

See S3 script options:

```bash
python3 scripts/s3_documents.py --help
```

Expected result: help text showing `--list` and `--upload`.

Real S3 list command:

```bash
python3 scripts/s3_documents.py --list
```

Expected result: documents listed from the configured S3 bucket and prefix.

Real S3 upload command:

```bash
python3 scripts/s3_documents.py --upload
```

Expected result: local PDFs from `data/raw/` uploaded to the configured S3 bucket and prefix.

### 9. Common Mistakes And How To Fix Them

Mistake: Thinking S3 is a database.

Fix: S3 is object storage. It stores files, not vector embeddings or relational rows.

Mistake: Putting AWS access keys in code.

Fix: Never hard-code AWS keys. Use local AWS configuration, environment variables, IAM roles, or AWS Secrets Manager.

Mistake: Committing `.env` to GitHub.

Fix: Keep `.env` ignored. Only `.env.example` should be committed.

Mistake: Expecting S3 upload to work without AWS credentials.

Fix: Configure AWS credentials locally before running real S3 commands.

Mistake: Confusing S3 keys with local file paths.

Fix: An S3 key is the object's name inside the bucket. It looks like a path, but it is not a local folder path.

Mistake: Uploading private healthcare PDFs carelessly.

Fix: For real healthcare data, use encryption, least-privilege IAM, private buckets, audit logging, and HIPAA-aware architecture.

### 10. What We Will Build Next

In Version 15, I will add the AWS EC2 deployment path.

That means documenting and preparing how the Dockerized backend and frontend can run on an EC2 instance.

## Version 14 ChatGPT Summary

We completed Version 14 of the Enterprise Healthcare Document Intelligence RAG Platform. Version 14 added an AWS S3 storage path for healthcare source PDFs. It did not implement AWS EC2 deployment yet.

Files added include `backend/app/storage/__init__.py`, `backend/app/storage/s3_storage.py`, `scripts/s3_documents.py`, and `tests/test_s3_storage.py`.

The S3 storage module includes helper functions to build S3 object keys, create a boto3 S3 client, upload one PDF, upload multiple PDFs, and list documents under an S3 prefix. It also includes an `S3Document` dataclass for clean document metadata.

Settings were updated to include `AWS_REGION`, `AWS_S3_BUCKET_NAME`, and `AWS_S3_RAW_PREFIX`. The app version was updated to `0.14.0`. `requirements.txt` now includes `boto3`.

The S3 script can list documents with `python3 scripts/s3_documents.py --list` and upload local PDFs from `data/raw/` with `python3 scripts/s3_documents.py --upload`. Real S3 commands require AWS credentials configured locally and a real bucket name in `.env`. No AWS keys were hard-coded or requested in chat.

Tests use fake AWS clients, so they do not call real AWS. Verification included `python3 -m unittest discover -s tests`, which ran 52 tests successfully, `python3 scripts/health_check.py`, and `python3 scripts/s3_documents.py --help`.

Version 14 connects to the resume because it adds real AWS S3 storage-path code for the healthcare RAG platform. The next version will add the AWS EC2 deployment path.

## Version 14 Interview Preparation

### Most Likely Interview Questions

Question: What did you build in Version 14?

Short answer: I added an AWS S3 document storage path for healthcare PDFs.

Detailed answer: I added S3 helper functions for object-key creation, PDF upload, multiple PDF upload, and document listing. I also added environment-based AWS settings, a command-line script, and tests that use fake AWS clients.

Follow-up question: Did your tests call real AWS?

Answer: No. The tests use fake S3 clients so they are fast, safe, and do not require credentials.

What not to say: "I stored vectors in S3." In this version, S3 stores source PDFs. ChromaDB stores vectors.

### Theory Questions

Question: What is AWS S3?

Short answer: S3 is cloud object storage.

Detailed answer: S3 stores files as objects inside buckets. Each object has a key, which is like its name or path inside the bucket.

Question: What is a bucket?

Short answer: A bucket is a top-level storage container in S3.

Detailed answer: Objects are stored inside buckets. For this project, a bucket would store healthcare source PDFs.

Question: What is an S3 key?

Short answer: An S3 key is the object name inside a bucket.

Detailed answer: For example, `healthcare-documents/raw/policy.pdf` is an S3 key. It looks like a path, but it is an object name in S3.

### Coding Questions

Question: What does `build_s3_key` do?

Short answer: It builds a clean S3 object key from a prefix and file name.

Detailed answer: It removes extra slashes from the prefix, keeps only the file name from the local path, and returns a predictable key like `healthcare-documents/raw/file.pdf`.

Question: Why does `upload_pdf_to_s3` validate the file extension?

Short answer: Because this storage path is meant for PDFs.

Detailed answer: Validation helps catch mistakes early, such as accidentally uploading text files or unsupported formats through the PDF upload path.

Question: Why inject a fake S3 client in tests?

Short answer: To test our logic without calling real AWS.

Detailed answer: It lets us verify bucket names, keys, upload calls, and list behavior while keeping tests deterministic and free.

### Tricky Questions

Question: Where are AWS credentials stored?

Short answer: Not in the code.

Detailed answer: Credentials should come from secure local AWS configuration, environment variables, IAM roles on AWS, or a secrets manager. The project does not hard-code keys.

Question: Does S3 replace ChromaDB?

Short answer: No.

Detailed answer: S3 stores source documents. ChromaDB stores vector embeddings for semantic search.

Question: Is S3 HIPAA-compliant by default?

Short answer: No architecture is compliant by default.

Detailed answer: S3 can be part of a compliant architecture, but you need proper encryption, private access, IAM controls, audit logs, business agreements, retention policies, and security review.

### System Design Questions

Question: Where does S3 fit in the RAG pipeline?

Short answer: At the document storage layer before ingestion.

Detailed answer: PDFs can be uploaded to S3, then ingestion can read or download them, parse text, chunk content, create embeddings, store vectors, and support retrieval.

Question: Why not store PDFs only on EC2?

Short answer: EC2 storage is not the best long-term document store.

Detailed answer: S3 is more durable and better suited for object storage. EC2 can run the app, while S3 stores source documents.

### Resume Defense Questions

Question: Your resume mentions AWS S3. What exactly did you implement?

Short answer: I implemented S3 upload and listing support for healthcare PDFs.

Detailed answer: I added a storage layer using boto3, environment-based bucket and prefix settings, a CLI script for listing/uploading documents, and mocked unit tests to validate S3 behavior safely.

Strong resume-style explanation:

"Integrated AWS S3 as the cloud document storage path for healthcare PDFs, with boto3 upload/list helpers, secure environment-based configuration, and mocked tests."

### Why Did You Choose This Tool Questions

Question: Why S3?

Short answer: It is durable cloud object storage.

Detailed answer: For a document intelligence platform, source PDFs need a reliable storage location. S3 is commonly used for storing raw files before processing.

Question: Why boto3?

Short answer: It is the standard AWS SDK for Python.

Detailed answer: boto3 provides Python APIs for AWS services, including S3 upload, listing, and client creation.

### Limitations Questions

Question: What are the limitations of Version 14?

Short answer: It adds S3 support, but ingestion still mainly reads local PDFs.

Detailed answer: The project can upload and list S3 documents, but it does not yet automatically ingest directly from S3, handle presigned URLs, use IAM roles on EC2, or enforce production security policies.

### Production Improvement Questions

Question: How would you improve this in production?

Short answer: Add IAM roles, encryption, private buckets, logging, and direct S3 ingestion.

Detailed answer: I would use least-privilege IAM, block public access, enable bucket encryption, use versioning and lifecycle rules, log access with CloudTrail, validate file types, scan documents, and connect S3 events to async ingestion jobs.

### Red Flags To Avoid

Do not say:
- "S3 is my vector database."
- "I put AWS keys in `.env.example`."
- "S3 automatically makes healthcare data compliant."
- "EC2 and S3 are the same thing."

Better answer:

"S3 is the durable document storage layer. It stores source PDFs, while ChromaDB stores embeddings. For real healthcare production use, S3 must be configured with private access, encryption, least-privilege IAM, audit logging, and compliance review."

## Version 15: AWS EC2 Deployment Path

### 1. What We Built

Version 15 adds the AWS EC2 deployment path.

This means the project now includes the files and instructions needed to explain how the Dockerized FastAPI backend and Streamlit frontend can run on an EC2 server.

Version 15 includes:
- `deployment/ec2/README.md`
- `deployment/ec2/user_data.sh`
- `docker-compose.ec2.yml`
- `scripts/validate_ec2_deployment.py`
- `tests/test_ec2_deployment.py`

Version 15 does not actually launch an EC2 instance from this local machine.

That is important to say honestly. We prepared the deployment path, but we did not claim a live AWS deployment.

### 2. Why We Built It

The project already had Docker in Version 13 and S3 in Version 14.

EC2 is the next logical step because EC2 can run the Docker containers on an AWS virtual server.

In simple words:
- Docker packages the app.
- S3 stores source PDFs.
- EC2 runs the app on a cloud server.

This version helps connect the local project to a realistic cloud deployment story.

### 3. What Each File Or Folder Does

`deployment/ec2/README.md`

This explains the EC2 deployment path in beginner-friendly language.

It covers:
- what EC2 does
- recommended instance setup
- security group basics
- manual deployment steps
- environment variable examples
- production security notes

`deployment/ec2/user_data.sh`

This is a bootstrap script for an Ubuntu EC2 instance.

User data is a script that EC2 can run when the server starts for the first time.

This script installs:
- Docker
- Docker Compose plugin
- Git
- required package setup tools

It does not contain real secrets.

`docker-compose.ec2.yml`

This is an EC2 override file.

It adds server-style settings on top of the normal local `docker-compose.yml`.

It adds:
- `restart: unless-stopped`
- `ENVIRONMENT=production`
- a named Docker volume called `healthcare_data`

`scripts/validate_ec2_deployment.py`

This checks that the EC2 deployment files exist and prints the recommended EC2 start command.

`tests/test_ec2_deployment.py`

This tests the EC2 deployment files without calling AWS.

The tests check:
- required files exist
- restart policies are present
- the EC2 volume exists
- the user data script installs Docker
- the user data script does not contain hard-coded secrets
- the EC2 README mentions security basics

### 4. How The Code Works In Simple Words

The base Compose file still defines the backend and frontend.

The EC2 Compose file adds extra server behavior.

When both files are used together:

```bash
docker compose -f docker-compose.yml -f docker-compose.ec2.yml up -d --build
```

Docker Compose merges them.

The backend still runs on port `8000`.

The frontend still runs on port `8501`.

The EC2 override tells Docker:
- keep containers running unless stopped
- run the backend in production mode
- store `/app/data` in a named Docker volume

The user data script prepares a fresh Ubuntu EC2 instance by installing Docker.

### 5. How This Step Connects To The Full RAG Pipeline

Before Version 15, the full RAG platform could run locally and inside Docker.

After Version 15, the project has a cloud server deployment path.

The full pipeline now looks like this:

PDFs in S3 or local data -> parsing with PyPDF, Unstructured, or OCR -> LangChain documents -> chunks -> OpenAI embeddings -> ChromaDB -> semantic retrieval -> grounded LLM answer -> citations -> FastAPI -> Streamlit -> Docker -> EC2

EC2 does not change the RAG algorithm.

EC2 is the cloud runtime layer.

### 6. How This Step Connects To My Resume

The resume stack includes AWS EC2.

Version 15 honestly supports that because the project now includes:
- EC2 deployment guide
- EC2 user data bootstrap script
- Docker Compose EC2 override
- deployment validation script
- tests for deployment configuration

Strong resume-style explanation:

"Prepared an AWS EC2 deployment path for a Dockerized healthcare RAG platform, including an Ubuntu bootstrap script, Compose production override, environment guidance, and deployment validation tests."

### 7. What Changed From Version 14

Version 14 added S3 document storage support.

Version 15 adds EC2 deployment preparation.

Before Version 15, the project had cloud storage support but no server deployment path.

After Version 15, the project explains how to run the Dockerized app on EC2.

### 8. What Output I Should Expect

Run tests:

```bash
python3 -m unittest discover -s tests
```

Expected result: all tests pass.

Run the health check:

```bash
python3 scripts/health_check.py
```

Expected result: app version `0.15.0` and status `ok`.

Validate EC2 deployment files:

```bash
python3 scripts/validate_ec2_deployment.py
```

Expected result: status `ok` and a recommended Docker Compose start command.

Validate combined Compose config:

```bash
docker compose -f docker-compose.yml -f docker-compose.ec2.yml config
```

Expected result: Docker Compose shows backend and frontend services with restart policies and the `healthcare_data` volume.

### 9. Common Mistakes And How To Fix Them

Mistake: Saying the app is deployed to EC2 when it has only a deployment path.

Fix: Say, "I prepared the EC2 deployment path. I can deploy it by following the documented steps."

Mistake: Putting real secrets in `user_data.sh`.

Fix: Do not put real API keys in user data. Use secure environment setup, IAM roles, or secret management.

Mistake: Exposing ports `8000` and `8501` publicly.

Fix: For testing, restrict access to your IP. For production, use HTTPS, authentication, and a reverse proxy or load balancer.

Mistake: Expecting EC2 to store documents permanently by itself.

Fix: Use S3 for source PDFs and a persistent Docker volume or managed storage for local application data.

Mistake: Forgetting Docker on EC2.

Fix: Use `deployment/ec2/user_data.sh` to install Docker and the Docker Compose plugin.

### 10. What We Will Build Next

The original resume-aligned roadmap is now complete through:
- PyPDF ingestion
- Unstructured parsing
- OCR fallback
- LangChain documents and splitting
- OpenAI embeddings
- ChromaDB
- retrieval
- grounded answers with citations
- FastAPI
- Streamlit
- RAGAS
- Docker
- AWS S3 path
- AWS EC2 path

Next, I would recommend a hardening version rather than adding another resume keyword.

Good next options:
- Version 16: production hardening checklist
- Version 16: GitHub setup and first clean commit
- Version 16: real local end-to-end run with your own PDFs and API key
- Version 16: direct S3-to-ingestion integration
- Version 16: authentication and request logging

## Version 15 ChatGPT Summary

We completed Version 15 of the Enterprise Healthcare Document Intelligence RAG Platform. Version 15 added an AWS EC2 deployment path. It did not actually launch a live EC2 instance.

Files added include `deployment/ec2/README.md`, `deployment/ec2/user_data.sh`, `docker-compose.ec2.yml`, `scripts/validate_ec2_deployment.py`, and `tests/test_ec2_deployment.py`.

The EC2 README explains the deployment approach in beginner-friendly language. It describes EC2 as the cloud server runtime, Docker as the packaging layer, S3 as the source PDF storage layer, and Docker Compose as the way to run backend and frontend services together.

The EC2 user data script installs Docker, Docker Compose plugin, Git, and required package setup tools on an Ubuntu EC2 instance. It does not contain real secrets.

The EC2 Compose override adds production-oriented runtime settings: `restart: unless-stopped`, `ENVIRONMENT=production`, and a named Docker volume called `healthcare_data`.

The validation script checks that EC2 deployment files exist and prints the recommended EC2 start command:

`docker compose -f docker-compose.yml -f docker-compose.ec2.yml up -d --build`

The app version was updated to `0.15.0`. Verification included `python3 -m unittest discover -s tests`, which ran 56 tests successfully, `python3 scripts/health_check.py`, `python3 scripts/validate_ec2_deployment.py`, and `docker compose -f docker-compose.yml -f docker-compose.ec2.yml config`.

Version 15 connects to the resume because it adds an honest AWS EC2 deployment path for the Dockerized healthcare RAG platform.

## Version 15 Interview Preparation

### Most Likely Interview Questions

Question: What did you build in Version 15?

Short answer: I prepared the AWS EC2 deployment path for the Dockerized RAG platform.

Detailed answer: I added an EC2 deployment guide, a user data bootstrap script for installing Docker on Ubuntu EC2, a Docker Compose EC2 override, a validation script, and tests for the deployment configuration.

Follow-up question: Did you actually deploy this to AWS?

Answer: In this version, I prepared the deployment path. I did not claim a live EC2 deployment. The files are ready to support a manual EC2 deployment.

What not to say: "I fully deployed production healthcare software to AWS." That overclaims.

### Theory Questions

Question: What is EC2?

Short answer: EC2 is a virtual server in AWS.

Detailed answer: EC2 lets me rent a cloud machine where I can install Docker and run the backend and frontend containers.

Question: What is user data in EC2?

Short answer: It is a startup script for a new EC2 instance.

Detailed answer: EC2 can run user data when the instance boots. In this project, the user data script installs Docker and prepares the server.

Question: How is EC2 different from S3?

Short answer: EC2 runs applications. S3 stores files.

Detailed answer: EC2 is compute. S3 is object storage. In this project, EC2 would run the app containers, while S3 stores source PDFs.

### Coding Questions

Question: What does `docker-compose.ec2.yml` add?

Short answer: It adds EC2/server-specific Compose settings.

Detailed answer: It adds restart policies, sets `ENVIRONMENT=production`, and uses a named Docker volume for application data.

Question: What does `validate_ec2_deployment.py` do?

Short answer: It checks that the deployment files exist.

Detailed answer: It returns a validation report showing the EC2 README, user data script, base Compose file, and EC2 Compose override are present.

### Tricky Questions

Question: Should API keys go in `user_data.sh`?

Short answer: No.

Detailed answer: User data can be visible in instance metadata or logs. Secrets should be handled through secure environment setup, IAM roles, SSM Parameter Store, Secrets Manager, or a controlled deployment process.

Question: Is exposing Streamlit on port `8501` production-ready?

Short answer: No.

Detailed answer: Direct public exposure is only acceptable for limited testing with restricted IP access. Production should use HTTPS, authentication, and controlled networking.

Question: Does EC2 make the app scalable automatically?

Short answer: No.

Detailed answer: A single EC2 instance is simple but limited. For scaling, I would consider a load balancer, autoscaling, ECS, or another container orchestration approach.

### System Design Questions

Question: How would the full system run on AWS?

Short answer: EC2 runs Docker containers, S3 stores PDFs, and the app uses OpenAI and ChromaDB for RAG.

Detailed answer: Users access Streamlit, Streamlit calls FastAPI, FastAPI performs retrieval and answer generation, PDFs can be stored in S3, and ChromaDB persists vector data in the mounted application data volume or a more robust managed storage layer.

Question: What would you improve before real production?

Short answer: Add HTTPS, auth, IAM roles, monitoring, backups, and CI/CD.

Detailed answer: I would put the app behind a reverse proxy or load balancer, add authentication, use IAM roles instead of long-lived keys, move secrets to AWS Secrets Manager or SSM, configure logs and metrics, add backups, and automate deployments.

### Resume Defense Questions

Question: Your resume mentions AWS EC2. What exactly did you implement?

Short answer: I implemented the EC2 deployment path for the Dockerized app.

Detailed answer: I added an EC2 deployment guide, an Ubuntu bootstrap script, a Compose override for server runtime settings, and tests that validate the deployment configuration.

Strong resume-style explanation:

"Prepared an AWS EC2 deployment path for a Dockerized healthcare RAG platform, including server bootstrap automation, Compose production overrides, and deployment validation tests."

### Why Did You Choose This Tool Questions

Question: Why EC2?

Short answer: It is a simple way to run Docker containers on AWS.

Detailed answer: EC2 is beginner-friendly for understanding server deployment because I can install Docker, run Compose, inspect logs, and learn the infrastructure pieces directly.

Question: Why not ECS?

Short answer: EC2 is simpler for this learning version.

Detailed answer: ECS is more production-scalable, but EC2 helps me understand the deployment basics first. A future improvement could move the containers to ECS.

### Limitations Questions

Question: What are the limitations of Version 15?

Short answer: It is a deployment path, not a live production deployment.

Detailed answer: It does not create AWS resources automatically, configure HTTPS, set up a domain, add authentication, configure CI/CD, use ECR, or manage secrets with AWS Secrets Manager.

### Production Improvement Questions

Question: How would you improve this for production?

Short answer: Use CI/CD, ECR, IAM roles, HTTPS, monitoring, and stronger security.

Detailed answer: I would push Docker images to ECR, deploy through CI/CD, use IAM roles, store secrets in Secrets Manager or SSM, use an Application Load Balancer with HTTPS, add auth, set up CloudWatch logs and metrics, and define infrastructure with Terraform or CloudFormation.

### Red Flags To Avoid

Do not say:
- "EC2 stores my PDFs."
- "User data is a good place for API keys."
- "Opening ports to everyone is fine."
- "This is fully HIPAA production-ready."
- "EC2 automatically scales my app."

Better answer:

"EC2 is the compute layer where the Dockerized app can run. S3 stores documents, Docker packages services, and EC2 hosts the containers. For real production, I would add IAM roles, HTTPS, authentication, monitoring, backups, CI/CD, and compliance review."
