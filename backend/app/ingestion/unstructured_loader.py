"""PDF ingestion utilities using Unstructured."""

from collections import defaultdict
from pathlib import Path
from typing import Callable, Iterable, List

from backend.app.ingestion.pdf_loader import ParsedPDFPage


class UnstructuredParserUnavailableError(ImportError):
    """Raised when Unstructured PDF parsing dependencies are unavailable."""


PartitionPDFCallable = Callable[..., Iterable[object]]


def _load_partition_pdf() -> PartitionPDFCallable:
    """Import Unstructured's PDF partitioner only when it is needed."""

    try:
        from unstructured.partition.pdf import partition_pdf
    except ImportError as error:
        raise UnstructuredParserUnavailableError(
            "Unstructured PDF parsing is not fully available. Install the missing "
            "PDF dependencies for your machine, then try again. On macOS this can "
            "include system libraries required by packages such as pi-heif/libheif."
        ) from error

    return partition_pdf


def _get_page_number(element: object) -> int:
    """Read page number metadata from an Unstructured element."""

    metadata = getattr(element, "metadata", None)
    page_number = getattr(metadata, "page_number", None)

    if page_number is None:
        return 1

    return int(page_number)


def load_pdf_pages_with_unstructured(
    pdf_path: Path,
    partitioner: PartitionPDFCallable = None,
) -> List[ParsedPDFPage]:
    """Extract text from a PDF using Unstructured and keep page metadata."""

    path = Path(pdf_path)

    if not path.exists():
        raise FileNotFoundError(f"PDF file not found: {path}")

    if path.suffix.lower() != ".pdf":
        raise ValueError(f"Expected a PDF file, received: {path}")

    active_partitioner = partitioner or _load_partition_pdf()
    elements = active_partitioner(filename=str(path))
    text_by_page = defaultdict(list)

    for element in elements:
        text = str(element).strip()

        if not text:
            continue

        text_by_page[_get_page_number(element)].append(text)

    if not text_by_page:
        return []

    total_pages = max(text_by_page.keys())

    return [
        ParsedPDFPage(
            text="\n\n".join(text_by_page[page_number]),
            file_name=path.name,
            file_path=str(path),
            page_number=page_number,
            total_pages=total_pages,
        )
        for page_number in sorted(text_by_page)
    ]


def load_pdfs_from_directory_with_unstructured(
    directory: Path,
    partitioner: PartitionPDFCallable = None,
) -> List[ParsedPDFPage]:
    """Extract pages from every PDF in a directory using Unstructured."""

    pdf_dir = Path(directory)

    if not pdf_dir.exists():
        raise FileNotFoundError(f"PDF directory not found: {pdf_dir}")

    parsed_pages: List[ParsedPDFPage] = []

    for pdf_path in sorted(pdf_dir.glob("*.pdf")):
        parsed_pages.extend(
            load_pdf_pages_with_unstructured(
                pdf_path=pdf_path,
                partitioner=partitioner,
            )
        )

    return parsed_pages

