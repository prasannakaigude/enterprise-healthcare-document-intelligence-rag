"""Semantic retrieval utilities for ChromaDB."""

from dataclasses import dataclass
from pathlib import Path
from typing import List

from langchain_core.documents import Document
from langchain_core.embeddings import Embeddings

from backend.app.rag.vector_store import create_chroma_vector_store


@dataclass(frozen=True)
class RetrievedChunk:
    """One retrieved chunk with citation metadata."""

    text: str
    score: float
    file_name: str
    page_number: int
    chunk_id: str
    metadata: dict


def _document_to_retrieved_chunk(document: Document, score: float) -> RetrievedChunk:
    """Convert a LangChain Document search result into a retrieved chunk."""

    metadata = dict(document.metadata)

    return RetrievedChunk(
        text=document.page_content,
        score=score,
        file_name=str(metadata.get("file_name", metadata.get("source", "unknown"))),
        page_number=int(metadata.get("page_number", 0)),
        chunk_id=str(metadata.get("chunk_id", "unknown")),
        metadata=metadata,
    )


def retrieve_relevant_chunks(
    query: str,
    embeddings: Embeddings,
    persist_directory: Path,
    collection_name: str,
    top_k: int = 4,
) -> List[RetrievedChunk]:
    """Search ChromaDB for chunks that are semantically similar to the query."""

    if not query.strip():
        raise ValueError("query cannot be empty")

    if top_k <= 0:
        raise ValueError("top_k must be greater than 0")

    vector_store = create_chroma_vector_store(
        embeddings=embeddings,
        persist_directory=persist_directory,
        collection_name=collection_name,
    )

    results = vector_store.similarity_search_with_score(query, k=top_k)

    return [
        _document_to_retrieved_chunk(document=document, score=score)
        for document, score in results
    ]

