"""PDF ingestion utilities using PyPDF."""

from dataclasses import dataclass
from pathlib import Path
from typing import List

from pypdf import PdfReader


@dataclass(frozen=True)
class ParsedPDFPage:
    """Text and metadata extracted from one PDF page."""

    text: str
    file_name: str
    file_path: str
    page_number: int
    total_pages: int


def load_pdf_pages(pdf_path: Path) -> List[ParsedPDFPage]:
    """Extract text from a PDF and keep page-level metadata."""

    path = Path(pdf_path)

    if not path.exists():
        raise FileNotFoundError(f"PDF file not found: {path}")

    if path.suffix.lower() != ".pdf":
        raise ValueError(f"Expected a PDF file, received: {path}")

    reader = PdfReader(str(path))
    total_pages = len(reader.pages)
    parsed_pages: List[ParsedPDFPage] = []

    for index, page in enumerate(reader.pages, start=1):
        text = page.extract_text() or ""
        parsed_pages.append(
            ParsedPDFPage(
                text=text.strip(),
                file_name=path.name,
                file_path=str(path),
                page_number=index,
                total_pages=total_pages,
            )
        )

    return parsed_pages


def load_pdfs_from_directory(directory: Path) -> List[ParsedPDFPage]:
    """Extract pages from every PDF in a directory."""

    pdf_dir = Path(directory)

    if not pdf_dir.exists():
        raise FileNotFoundError(f"PDF directory not found: {pdf_dir}")

    parsed_pages: List[ParsedPDFPage] = []

    for pdf_path in sorted(pdf_dir.glob("*.pdf")):
        parsed_pages.extend(load_pdf_pages(pdf_path))

    return parsed_pages

