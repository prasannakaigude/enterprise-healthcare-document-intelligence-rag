"""API request and response models."""

from typing import List, Optional

from pydantic import BaseModel, Field


class AskRequest(BaseModel):
    """Question request sent to the RAG backend."""

    question: str = Field(..., min_length=1)
    file_name: Optional[str] = None


class DocumentResponse(BaseModel):
    """Document available for scoped retrieval."""

    file_name: str


class CitationResponse(BaseModel):
    """Source citation returned with an answer."""

    file_name: str
    page_number: int
    chunk_id: str


class AskResponse(BaseModel):
    """Grounded answer response."""

    answer: str
    citations: List[CitationResponse]


class IndexResponse(BaseModel):
    """Response returned after rebuilding the vector store."""

    pdf_pages_parsed: int
    documents_created: int
    chunks_created: int
    chunks_stored: int
    collection_name: str


class HealthResponse(BaseModel):
    """Basic API health response."""

    status: str
    app_name: str
    app_version: str
    environment: str
