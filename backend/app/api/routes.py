"""FastAPI routes for the healthcare RAG backend."""

from fastapi import APIRouter, HTTPException

from backend.app.core.health import get_health_status
from backend.app.models.api import (
    AskRequest,
    AskResponse,
    CitationResponse,
    HealthResponse,
)
from backend.app.rag.pipeline import answer_question


router = APIRouter()


@router.get("/health", response_model=HealthResponse)
def health_check() -> HealthResponse:
    """Return backend health status."""

    status = get_health_status()

    return HealthResponse(
        status=str(status["status"]),
        app_name=str(status["app_name"]),
        app_version=str(status["app_version"]),
        environment=str(status["environment"]),
    )


@router.post("/ask", response_model=AskResponse)
def ask_question(request: AskRequest) -> AskResponse:
    """Answer a user question using the RAG pipeline."""

    try:
        grounded_answer = answer_question(request.question)
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error)) from error

    return AskResponse(
        answer=grounded_answer.answer,
        citations=[
            CitationResponse(
                file_name=citation.file_name,
                page_number=citation.page_number,
                chunk_id=citation.chunk_id,
            )
            for citation in grounded_answer.citations
        ],
    )

