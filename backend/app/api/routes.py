"""FastAPI routes for the healthcare RAG backend."""

from typing import List

from fastapi import APIRouter, HTTPException

from backend.app.core.conversation_logger import write_conversation_log
from backend.app.core.health import get_health_status
from backend.app.core.settings import get_settings
from backend.app.models.api import (
    AskRequest,
    AskResponse,
    CitationResponse,
    DocumentResponse,
    HealthResponse,
    IndexResponse,
)
from backend.app.rag.indexing import rebuild_vector_store
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
        grounded_answer = answer_question(
            question=request.question,
            file_name=request.file_name,
        )
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error)) from error

    write_conversation_log(
        question=request.question,
        answer=grounded_answer.answer,
        citations=grounded_answer.citations,
        settings=get_settings(),
    )

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


@router.get("/documents", response_model=List[DocumentResponse])
def list_documents() -> List[DocumentResponse]:
    """List local raw PDFs that can be selected in the UI."""

    settings = get_settings()
    return [
        DocumentResponse(file_name=pdf_path.name)
        for pdf_path in sorted(settings.raw_data_dir.glob("*.pdf"))
    ]


@router.post("/ingest/rebuild", response_model=IndexResponse)
def rebuild_documents() -> IndexResponse:
    """Rebuild the vector store from uploaded raw PDFs."""

    try:
        result = rebuild_vector_store(get_settings())
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error)) from error

    return IndexResponse(
        pdf_pages_parsed=result.pdf_pages_parsed,
        documents_created=result.documents_created,
        chunks_created=result.chunks_created,
        chunks_stored=result.chunks_stored,
        collection_name=result.collection_name,
    )
