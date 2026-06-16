"""Parse PDFs from the local raw data folder using Unstructured."""

from pathlib import Path
import sys


PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from backend.app.core.settings import get_settings
from backend.app.ingestion.unstructured_loader import (
    UnstructuredParserUnavailableError,
    load_pdfs_from_directory_with_unstructured,
)


def main() -> None:
    """Load PDFs from data/raw with Unstructured and print a summary."""

    settings = get_settings()

    try:
        parsed_pages = load_pdfs_from_directory_with_unstructured(settings.raw_data_dir)
    except UnstructuredParserUnavailableError as error:
        print(str(error))
        return

    print(f"PDF directory: {settings.raw_data_dir}")
    print(f"PDF pages parsed with Unstructured: {len(parsed_pages)}")

    for page in parsed_pages:
        preview = page.text[:120].replace("\n", " ")
        print(
            f"- {page.file_name} | page {page.page_number}/{page.total_pages} | "
            f"{len(page.text)} characters | {preview}"
        )


if __name__ == "__main__":
    main()

