"""Convert parsed PDF pages into LangChain documents and chunks."""

from typing import Iterable, List
import warnings


warnings.filterwarnings("ignore", message="urllib3 v2 only supports OpenSSL.*")

from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter

from backend.app.ingestion.pdf_loader import ParsedPDFPage


def pages_to_documents(pages: Iterable[ParsedPDFPage]) -> List[Document]:
    """Convert parsed PDF pages into LangChain Document objects."""

    documents: List[Document] = []

    for page in pages:
        if not page.text.strip():
            continue

        documents.append(
            Document(
                page_content=page.text,
                metadata={
                    "source": page.file_name,
                    "file_name": page.file_name,
                    "file_path": page.file_path,
                    "page_number": page.page_number,
                    "total_pages": page.total_pages,
                },
            )
        )

    return documents


def split_documents(
    documents: Iterable[Document],
    chunk_size: int = 1000,
    chunk_overlap: int = 200,
) -> List[Document]:
    """Split LangChain documents into smaller chunks."""

    if chunk_size <= 0:
        raise ValueError("chunk_size must be greater than 0")

    if chunk_overlap < 0:
        raise ValueError("chunk_overlap cannot be negative")

    if chunk_overlap >= chunk_size:
        raise ValueError("chunk_overlap must be smaller than chunk_size")

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
    )

    chunks: List[Document] = []

    for document in documents:
        split_chunks = splitter.split_documents([document])

        for index, chunk in enumerate(split_chunks, start=1):
            metadata = dict(chunk.metadata)
            metadata["chunk_number"] = index
            metadata["chunk_id"] = (
                f"{metadata.get('file_name', 'unknown')}:"
                f"page-{metadata.get('page_number', 'unknown')}:"
                f"chunk-{index}"
            )
            chunks.append(
                Document(
                    page_content=chunk.page_content,
                    metadata=metadata,
                )
            )

    return chunks
