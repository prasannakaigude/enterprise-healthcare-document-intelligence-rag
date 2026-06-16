"""Build a local ChromaDB vector store from PDFs in data/raw."""

from pathlib import Path
import sys


PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from backend.app.core.settings import get_settings
from backend.app.rag.indexing import rebuild_vector_store


def main() -> None:
    """Create embeddings for chunks and store them in local ChromaDB."""

    settings = get_settings()
    result = rebuild_vector_store(settings)

    print(f"PDF directory: {settings.raw_data_dir}")
    print(f"PDF pages parsed: {result.pdf_pages_parsed}")
    print(f"LangChain documents created: {result.documents_created}")
    print(f"Text chunks created: {result.chunks_created}")

    if not result.chunks_created:
        print("No chunks found. Add text-based PDFs to data/raw before embedding.")
        return

    print(f"ChromaDB directory: {settings.chroma_db_dir}")
    print(f"ChromaDB collection: {result.collection_name}")
    print(f"Chunks stored: {result.chunks_stored}")


if __name__ == "__main__":
    main()
