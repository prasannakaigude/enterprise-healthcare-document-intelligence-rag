"""Local conversation logging utilities."""

from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
from typing import Any, Iterable, Optional

from backend.app.core.settings import Settings, get_settings
from backend.app.rag.answer_generator import SourceCitation


def _sha256_text(text: str) -> str:
    """Create a stable hash without storing raw text."""

    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def _citation_to_dict(citation: SourceCitation) -> dict[str, Any]:
    """Convert a citation object into JSON-serializable metadata."""

    return {
        "file_name": citation.file_name,
        "page_number": citation.page_number,
        "chunk_id": citation.chunk_id,
    }


def build_conversation_log_record(
    question: str,
    answer: str,
    citations: Iterable[SourceCitation],
    settings: Settings = None,
) -> dict[str, Any]:
    """Build one local conversation log record."""

    active_settings = settings or get_settings()
    citation_list = list(citations)
    record: dict[str, Any] = {
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "environment": active_settings.environment,
        "question_hash": _sha256_text(question),
        "answer_hash": _sha256_text(answer),
        "citation_count": len(citation_list),
        "citations": [_citation_to_dict(citation) for citation in citation_list],
        "raw_text_saved": active_settings.log_raw_conversation_text,
    }

    if active_settings.log_raw_conversation_text:
        record["question"] = question
        record["answer"] = answer

    return record


def write_conversation_log(
    question: str,
    answer: str,
    citations: Iterable[SourceCitation],
    settings: Settings = None,
) -> Optional[Path]:
    """Append one conversation record to a local JSONL file."""

    active_settings = settings or get_settings()

    if not active_settings.log_conversations:
        return None

    log_path = active_settings.conversation_log_path
    log_path.parent.mkdir(parents=True, exist_ok=True)
    record = build_conversation_log_record(
        question=question,
        answer=answer,
        citations=citations,
        settings=active_settings,
    )

    with log_path.open("a", encoding="utf-8") as log_file:
        log_file.write(json.dumps(record, sort_keys=True) + "\n")

    return log_path
