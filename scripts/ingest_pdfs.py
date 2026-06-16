"""Parse PDFs from the local raw data folder using PyPDF."""

from pathlib import Path
import sys


PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from backend.app.core.settings import get_settings
from backend.app.ingestion.pdf_loader import load_pdfs_from_directory


def main() -> None:
    """Load PDFs from data/raw and print a simple ingestion summary."""

    settings = get_settings()
    parsed_pages = load_pdfs_from_directory(settings.raw_data_dir)

    print(f"PDF directory: {settings.raw_data_dir}")
    print(f"PDF pages parsed: {len(parsed_pages)}")

    for page in parsed_pages:
        preview = page.text[:120].replace("\n", " ")
        print(
            f"- {page.file_name} | page {page.page_number}/{page.total_pages} | "
            f"{len(page.text)} characters | {preview}"
        )


if __name__ == "__main__":
    main()

