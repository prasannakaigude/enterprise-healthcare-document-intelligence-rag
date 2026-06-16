"""Helpers for saving uploaded PDFs from the Streamlit UI."""

from pathlib import Path
import re
from typing import BinaryIO


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_RAW_DATA_DIR = PROJECT_ROOT / "data" / "raw"


def sanitize_pdf_filename(file_name: str) -> str:
    """Return a safe local PDF file name."""

    original_name = Path(file_name).name
    cleaned_name = re.sub(r"[^A-Za-z0-9._-]+", "_", original_name).strip("._")

    if not cleaned_name:
        raise ValueError("Uploaded file name cannot be empty.")

    if not cleaned_name.lower().endswith(".pdf"):
        raise ValueError("Only PDF files can be uploaded.")

    return cleaned_name


def _next_available_path(raw_data_dir: Path, file_name: str) -> Path:
    """Avoid overwriting an existing local PDF."""

    candidate_path = raw_data_dir / file_name

    if not candidate_path.exists():
        return candidate_path

    stem = candidate_path.stem
    suffix = candidate_path.suffix

    for index in range(1, 1000):
        numbered_path = raw_data_dir / f"{stem}_{index}{suffix}"
        if not numbered_path.exists():
            return numbered_path

    raise FileExistsError(f"Too many files with the same name: {file_name}")


def save_uploaded_pdf(
    uploaded_file: BinaryIO,
    raw_data_dir: Path = DEFAULT_RAW_DATA_DIR,
) -> Path:
    """Save an uploaded PDF into the local raw data folder."""

    raw_data_dir.mkdir(parents=True, exist_ok=True)
    safe_file_name = sanitize_pdf_filename(uploaded_file.name)
    destination_path = _next_available_path(raw_data_dir, safe_file_name)

    uploaded_file.seek(0)
    destination_path.write_bytes(uploaded_file.read())

    return destination_path
