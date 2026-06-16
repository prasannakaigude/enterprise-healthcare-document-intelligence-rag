"""Parse local PDFs and split extracted text into LangChain chunks."""

from pathlib import Path
import sys


PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from backend.app.core.settings import get_settings
from backend.app.ingestion.pdf_loader import load_pdfs_from_directory
from backend.app.rag.document_processing import pages_to_documents, split_documents


def main() -> None:
    """Load PDFs, create LangChain documents, and print chunk summaries."""

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

    for chunk in chunks:
        preview = chunk.page_content[:120].replace("\n", " ")
        print(
            f"- {chunk.metadata['chunk_id']} | "
            f"{len(chunk.page_content)} characters | {preview}"
        )


if __name__ == "__main__":
    main()
