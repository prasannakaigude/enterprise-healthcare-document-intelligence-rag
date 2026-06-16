"""List or upload healthcare PDFs using the configured AWS S3 path."""

from pathlib import Path
import argparse
import sys


PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from backend.app.core.settings import get_settings
from backend.app.storage.s3_storage import (
    create_s3_client,
    list_s3_documents,
    upload_pdfs_to_s3,
)


def main() -> None:
    """Run a safe S3 document command."""

    parser = argparse.ArgumentParser(description="Manage healthcare PDFs in S3.")
    parser.add_argument(
        "--upload",
        action="store_true",
        help="Upload local PDFs from RAW_DATA_DIR to S3.",
    )
    parser.add_argument(
        "--list",
        action="store_true",
        help="List documents already stored under the configured S3 prefix.",
    )
    args = parser.parse_args()

    settings = get_settings()

    if not settings.aws_s3_bucket_name:
        raise ValueError(
            "AWS_S3_BUCKET_NAME is required for S3 commands. "
            "Set it in your local .env file, not in chat."
        )

    s3_client = create_s3_client(settings.aws_region)

    if args.upload:
        pdf_paths = sorted(settings.raw_data_dir.glob("*.pdf"))
        uploaded_keys = upload_pdfs_to_s3(
            pdf_paths=pdf_paths,
            bucket_name=settings.aws_s3_bucket_name,
            prefix=settings.aws_s3_raw_prefix,
            s3_client=s3_client,
        )

        print(f"Uploaded PDFs: {len(uploaded_keys)}")
        for key in uploaded_keys:
            print(f"- s3://{settings.aws_s3_bucket_name}/{key}")
        return

    documents = list_s3_documents(
        bucket_name=settings.aws_s3_bucket_name,
        prefix=settings.aws_s3_raw_prefix,
        s3_client=s3_client,
    )

    print(f"S3 bucket: {settings.aws_s3_bucket_name}")
    print(f"S3 prefix: {settings.aws_s3_raw_prefix}")
    print(f"Documents found: {len(documents)}")

    for document in documents:
        print(
            f"- s3://{document.bucket}/{document.key} | "
            f"{document.size_bytes} bytes | {document.last_modified}"
        )


if __name__ == "__main__":
    main()
