"""Vector storage utilities for OpenAI embeddings and ChromaDB."""

from pathlib import Path
from typing import Iterable, List
import os
import warnings


warnings.filterwarnings("ignore", message="urllib3 v2 only supports OpenSSL.*")

from langchain_chroma import Chroma
from langchain_core.documents import Document
from langchain_core.embeddings import Embeddings
from langchain_openai import OpenAIEmbeddings

from backend.app.core.settings import Settings, get_settings


CHROMA_WRITE_BATCH_SIZE = 500


def batch_items(items: List, batch_size: int = CHROMA_WRITE_BATCH_SIZE) -> Iterable[List]:
    """Split a list into smaller batches for ChromaDB writes."""

    for start_index in range(0, len(items), batch_size):
        yield items[start_index : start_index + batch_size]


def create_openai_embeddings(settings: Settings = None) -> OpenAIEmbeddings:
    """Create the real OpenAI embedding client from environment settings."""

    active_settings = settings or get_settings()

    if not os.getenv("OPENAI_API_KEY"):
        raise ValueError(
            "OPENAI_API_KEY is not set. Create a local .env file or export the "
            "variable before running real OpenAI embeddings."
        )

    return OpenAIEmbeddings(model=active_settings.embedding_model)


def create_chroma_vector_store(
    embeddings: Embeddings,
    persist_directory: Path,
    collection_name: str,
) -> Chroma:
    """Create or load a persistent ChromaDB vector store."""

    return Chroma(
        collection_name=collection_name,
        embedding_function=embeddings,
        persist_directory=str(persist_directory),
    )


def store_documents_in_chroma(
    documents: Iterable[Document],
    embeddings: Embeddings,
    persist_directory: Path,
    collection_name: str,
) -> Chroma:
    """Embed documents and store them in ChromaDB."""

    document_list: List[Document] = list(documents)
    vector_store = create_chroma_vector_store(
        embeddings=embeddings,
        persist_directory=persist_directory,
        collection_name=collection_name,
    )

    if document_list:
        ids = [
            str(document.metadata.get("chunk_id", f"chunk-{index}"))
            for index, document in enumerate(document_list, start=1)
        ]
        try:
            for id_batch in batch_items(ids):
                vector_store.delete(ids=id_batch)
        except Exception:
            pass
        for document_batch, id_batch in zip(
            batch_items(document_list),
            batch_items(ids),
        ):
            vector_store.add_documents(document_batch, ids=id_batch)

    return vector_store
