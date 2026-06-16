"""Save parsed pages and chunks for local inspection."""

from dataclasses import asdict
import json
from pathlib import Path
from typing import Iterable

from langchain_core.documents import Document

from backend.app.ingestion.pdf_loader import ParsedPDFPage


def _write_jsonl(records: Iterable[dict], output_path: Path) -> Path:
    """Write records as JSON lines."""

    output_path.parent.mkdir(parents=True, exist_ok=True)

    with output_path.open("w", encoding="utf-8") as output_file:
        for record in records:
            output_file.write(json.dumps(record, ensure_ascii=True, sort_keys=True) + "\n")

    return output_path


def save_parsed_pages_jsonl(
    pages: Iterable[ParsedPDFPage],
    processed_data_dir: Path,
) -> Path:
    """Save extracted PDF pages to a local JSONL file."""

    output_path = processed_data_dir / "parsed_pages.jsonl"
    records = (asdict(page) for page in pages)
    return _write_jsonl(records, output_path)


def save_chunks_jsonl(
    chunks: Iterable[Document],
    processed_data_dir: Path,
) -> Path:
    """Save text chunks and metadata to a local JSONL file."""

    output_path = processed_data_dir / "chunks.jsonl"
    records = (
        {
            "text": chunk.page_content,
            "metadata": dict(chunk.metadata),
        }
        for chunk in chunks
    )
    return _write_jsonl(records, output_path)


def save_processed_artifacts(
    pages: Iterable[ParsedPDFPage],
    chunks: Iterable[Document],
    processed_data_dir: Path,
) -> tuple[Path, Path]:
    """Save parsed pages and chunks for debugging the RAG pipeline."""

    page_list = list(pages)
    chunk_list = list(chunks)

    pages_path = save_parsed_pages_jsonl(page_list, processed_data_dir)
    chunks_path = save_chunks_jsonl(chunk_list, processed_data_dir)

    return pages_path, chunks_path
