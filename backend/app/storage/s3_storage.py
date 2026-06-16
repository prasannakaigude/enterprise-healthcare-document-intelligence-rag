"""AWS S3 storage helpers for healthcare source documents."""

from dataclasses import dataclass
from importlib import import_module
from pathlib import Path
from typing import Any, Iterable, List, Optional


@dataclass(frozen=True)
class S3Document:
    """Metadata for one document stored in S3."""

    bucket: str
    key: str
    size_bytes: int
    last_modified: str


def build_s3_key(file_name: str, prefix: str = "healthcare-documents/raw") -> str:
    """Build a predictable S3 object key for an uploaded source document."""

    clean_prefix = prefix.strip("/")
    clean_file_name = Path(file_name).name

    if not clean_file_name:
        raise ValueError("File name cannot be empty.")

    return f"{clean_prefix}/{clean_file_name}" if clean_prefix else clean_file_name


def create_s3_client(region_name: str, boto3_module: Optional[Any] = None) -> Any:
    """Create a boto3 S3 client without hard-coding credentials."""

    boto3 = boto3_module

    if boto3 is None:
        try:
            boto3 = import_module("boto3")
        except ModuleNotFoundError as exc:
            raise RuntimeError(
                "boto3 is not installed. Run `pip install -r requirements.txt` "
                "before using real AWS S3 commands."
            ) from exc

    return boto3.client("s3", region_name=region_name)


def upload_pdf_to_s3(
    local_pdf_path: Path,
    bucket_name: str,
    prefix: str,
    s3_client: Any,
) -> str:
    """Upload one local PDF to S3 and return the S3 key."""

    pdf_path = Path(local_pdf_path)

    if not bucket_name:
        raise ValueError("AWS S3 bucket name is required.")

    if not pdf_path.exists():
        raise FileNotFoundError(f"PDF file not found: {pdf_path}")

    if pdf_path.suffix.lower() != ".pdf":
        raise ValueError(f"Expected a PDF file, received: {pdf_path}")

    s3_key = build_s3_key(pdf_path.name, prefix)
    s3_client.upload_file(str(pdf_path), bucket_name, s3_key)

    return s3_key


def list_s3_documents(
    bucket_name: str,
    prefix: str,
    s3_client: Any,
) -> List[S3Document]:
    """List PDF-like source documents under an S3 prefix."""

    if not bucket_name:
        raise ValueError("AWS S3 bucket name is required.")

    paginator = s3_client.get_paginator("list_objects_v2")
    pages = paginator.paginate(Bucket=bucket_name, Prefix=prefix.strip("/"))
    documents: List[S3Document] = []

    for page in pages:
        for item in page.get("Contents", []):
            key = item["Key"]
            if key.endswith("/"):
                continue

            documents.append(
                S3Document(
                    bucket=bucket_name,
                    key=key,
                    size_bytes=int(item.get("Size", 0)),
                    last_modified=str(item.get("LastModified", "")),
                )
            )

    return documents


def upload_pdfs_to_s3(
    pdf_paths: Iterable[Path],
    bucket_name: str,
    prefix: str,
    s3_client: Any,
) -> List[str]:
    """Upload multiple PDFs and return their S3 keys."""

    uploaded_keys: List[str] = []

    for pdf_path in pdf_paths:
        uploaded_keys.append(
            upload_pdf_to_s3(
                local_pdf_path=pdf_path,
                bucket_name=bucket_name,
                prefix=prefix,
                s3_client=s3_client,
            )
        )

    return uploaded_keys
