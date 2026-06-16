"""Build a local ChromaDB vector store from PDFs in data/raw."""

from pathlib import Path
import sys


PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from backend.app.core.settings import get_settings
from backend.app.ingestion.pdf_loader import load_pdfs_from_directory
from backend.app.rag.document_processing import pages_to_documents, split_documents
from backend.app.rag.vector_store import create_openai_embeddings, store_documents_in_chroma


def main() -> None:
    """Create embeddings for chunks and store them in local ChromaDB."""

    settings = get_settings()
    parsed_pages = load_pdfs_from_directory(settings.raw_data_dir)
    documents = pages_to_documents(parsed_pages)
    chunks = split_documents(
        documents,
        chunk_size=settings.chunk_size,
        chunk_overlap=settings.chunk_overlap,
    )

    print(f"PDF directory: {settings.raw_data_dir}")
    print(f"PDF pages parsed: {len(parsed_pages)}")
    print(f"LangChain documents created: {len(documents)}")
    print(f"Text chunks created: {len(chunks)}")

    if not chunks:
        print("No chunks found. Add text-based PDFs to data/raw before embedding.")
        return

    embeddings = create_openai_embeddings(settings)
    vector_store = store_documents_in_chroma(
        documents=chunks,
        embeddings=embeddings,
        persist_directory=settings.chroma_db_dir,
        collection_name=settings.chroma_collection_name,
    )

    print(f"ChromaDB directory: {settings.chroma_db_dir}")
    print(f"ChromaDB collection: {settings.chroma_collection_name}")
    print(f"Chunks stored: {vector_store._collection.count()}")


if __name__ == "__main__":
    main()

