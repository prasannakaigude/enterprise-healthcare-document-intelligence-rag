"""API request and response models."""

from typing import List

from pydantic import BaseModel, Field


class AskRequest(BaseModel):
    """Question request sent to the RAG backend."""

    question: str = Field(..., min_length=1)


class CitationResponse(BaseModel):
    """Source citation returned with an answer."""

    file_name: str
    page_number: int
    chunk_id: str


class AskResponse(BaseModel):
    """Grounded answer response."""

    answer: str
    citations: List[CitationResponse]


class HealthResponse(BaseModel):
    """Basic API health response."""

    status: str
    app_name: str
    app_version: str
    environment: str

