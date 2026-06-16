"""OCR fallback utilities for scanned PDF pages."""

from pathlib import Path
from typing import Callable, Iterable, List

from backend.app.ingestion.pdf_loader import ParsedPDFPage, load_pdf_pages


class OCRUnavailableError(RuntimeError):
    """Raised when OCR system dependencies are unavailable."""


ImageConverter = Callable[..., Iterable[object]]
ImageToText = Callable[[object], str]


def _load_ocr_dependencies() -> tuple:
    """Import OCR dependencies only when OCR is needed."""

    try:
        from pdf2image import convert_from_path
        import pytesseract
    except ImportError as error:
        raise OCRUnavailableError(
            "OCR Python packages are not available. Install pdf2image and pytesseract."
        ) from error

    return convert_from_path, pytesseract.image_to_string


def load_pdf_pages_with_ocr(
    pdf_path: Path,
    image_converter: ImageConverter = None,
    image_to_text: ImageToText = None,
) -> List[ParsedPDFPage]:
    """Convert PDF pages to images and extract text with OCR."""

    path = Path(pdf_path)

    if not path.exists():
        raise FileNotFoundError(f"PDF file not found: {path}")

    if path.suffix.lower() != ".pdf":
        raise ValueError(f"Expected a PDF file, received: {path}")

    if image_converter is None or image_to_text is None:
        image_converter, image_to_text = _load_ocr_dependencies()

    try:
        images = list(image_converter(str(path)))
    except Exception as error:
        raise OCRUnavailableError(
            "OCR could not convert PDF pages to images. On macOS, install Poppler "
            "and make sure it is available on PATH."
        ) from error

    total_pages = len(images)
    parsed_pages: List[ParsedPDFPage] = []

    for index, image in enumerate(images, start=1):
        try:
            text = image_to_text(image) or ""
        except Exception as error:
            raise OCRUnavailableError(
                "OCR could not extract text from a page image. On macOS, install "
                "Tesseract and make sure it is available on PATH."
            ) from error

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


def load_pdf_pages_with_ocr_fallback(
    pdf_path: Path,
    image_converter: ImageConverter = None,
    image_to_text: ImageToText = None,
) -> List[ParsedPDFPage]:
    """Use PyPDF first, then OCR only for pages without extractable text."""

    pypdf_pages = load_pdf_pages(pdf_path)

    if all(page.text.strip() for page in pypdf_pages):
        return pypdf_pages

    ocr_pages = load_pdf_pages_with_ocr(
        pdf_path=pdf_path,
        image_converter=image_converter,
        image_to_text=image_to_text,
    )
    ocr_by_page = {page.page_number: page for page in ocr_pages}
    merged_pages: List[ParsedPDFPage] = []

    for page in pypdf_pages:
        if page.text.strip():
            merged_pages.append(page)
        else:
            merged_pages.append(ocr_by_page.get(page.page_number, page))

    return merged_pages


def load_pdfs_from_directory_with_ocr_fallback(
    directory: Path,
    image_converter: ImageConverter = None,
    image_to_text: ImageToText = None,
) -> List[ParsedPDFPage]:
    """Load every PDF in a directory using PyPDF with OCR fallback."""

    pdf_dir = Path(directory)

    if not pdf_dir.exists():
        raise FileNotFoundError(f"PDF directory not found: {pdf_dir}")

    parsed_pages: List[ParsedPDFPage] = []

    for pdf_path in sorted(pdf_dir.glob("*.pdf")):
        parsed_pages.extend(
            load_pdf_pages_with_ocr_fallback(
                pdf_path=pdf_path,
                image_converter=image_converter,
                image_to_text=image_to_text,
            )
        )

    return parsed_pages

