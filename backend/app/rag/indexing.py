"""Document indexing workflow for building the vector store."""

from dataclasses import dataclass

from backend.app.core.settings import Settings, get_settings
from backend.app.ingestion.pdf_loader import load_pdfs_from_directory
from backend.app.rag.document_processing import pages_to_documents, split_documents
from backend.app.rag.processed_artifacts import save_processed_artifacts
from backend.app.rag.vector_store import create_openai_embeddings, store_documents_in_chroma


@dataclass(frozen=True)
class IndexingResult:
    """Summary of one vector indexing run."""

    pdf_pages_parsed: int
    documents_created: int
    chunks_created: int
    chunks_stored: int
    collection_name: str


def rebuild_vector_store(settings: Settings = None) -> IndexingResult:
    """Rebuild or update ChromaDB from PDFs in the raw data folder."""

    active_settings = settings or get_settings()
    parsed_pages = load_pdfs_from_directory(active_settings.raw_data_dir)
    documents = pages_to_documents(parsed_pages)
    chunks = split_documents(
        documents,
        chunk_size=active_settings.chunk_size,
        chunk_overlap=active_settings.chunk_overlap,
    )
    save_processed_artifacts(
        pages=parsed_pages,
        chunks=chunks,
        processed_data_dir=active_settings.processed_data_dir,
    )

    if not chunks:
        return IndexingResult(
            pdf_pages_parsed=len(parsed_pages),
            documents_created=len(documents),
            chunks_created=0,
            chunks_stored=0,
            collection_name=active_settings.chroma_collection_name,
        )

    embeddings = create_openai_embeddings(active_settings)
    vector_store = store_documents_in_chroma(
        documents=chunks,
        embeddings=embeddings,
        persist_directory=active_settings.chroma_db_dir,
        collection_name=active_settings.chroma_collection_name,
    )

    return IndexingResult(
        pdf_pages_parsed=len(parsed_pages),
        documents_created=len(documents),
        chunks_created=len(chunks),
        chunks_stored=vector_store._collection.count(),
        collection_name=active_settings.chroma_collection_name,
    )
