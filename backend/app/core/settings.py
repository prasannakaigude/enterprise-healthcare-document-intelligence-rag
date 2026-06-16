"""Application settings for the healthcare RAG platform."""

from dataclasses import dataclass
from pathlib import Path
import os

from dotenv import load_dotenv


PROJECT_ROOT = Path(__file__).resolve().parents[3]
load_dotenv(PROJECT_ROOT / ".env")


@dataclass(frozen=True)
class Settings:
    """Small settings object used by the backend application."""

    app_name: str = "Enterprise Healthcare Document Intelligence RAG Platform"
    app_version: str = "0.15.0"
    environment: str = "local"
    aws_region: str = "us-east-1"
    aws_s3_bucket_name: str = ""
    aws_s3_raw_prefix: str = "healthcare-documents/raw"
    embedding_model: str = "text-embedding-3-small"
    chat_model: str = "gpt-4o-mini"
    chat_temperature: float = 0.0
    chroma_collection_name: str = "healthcare_documents"
    raw_data_dir: Path = PROJECT_ROOT / "data" / "raw"
    processed_data_dir: Path = PROJECT_ROOT / "data" / "processed"
    chroma_db_dir: Path = PROJECT_ROOT / "data" / "vector_db" / "chroma"
    chunk_size: int = 1000
    chunk_overlap: int = 200
    retrieval_top_k: int = 4


def get_settings() -> Settings:
    """Load settings from environment variables with safe local defaults."""

    return Settings(
        app_name=os.getenv(
            "APP_NAME",
            "Enterprise Healthcare Document Intelligence RAG Platform",
        ),
        app_version=os.getenv("APP_VERSION", "0.15.0"),
        environment=os.getenv("ENVIRONMENT", "local"),
        aws_region=os.getenv("AWS_REGION", "us-east-1"),
        aws_s3_bucket_name=os.getenv("AWS_S3_BUCKET_NAME", ""),
        aws_s3_raw_prefix=os.getenv(
            "AWS_S3_RAW_PREFIX",
            "healthcare-documents/raw",
        ),
        embedding_model=os.getenv("EMBEDDING_MODEL", "text-embedding-3-small"),
        chat_model=os.getenv("CHAT_MODEL", "gpt-4o-mini"),
        chat_temperature=float(os.getenv("CHAT_TEMPERATURE", "0")),
        chroma_collection_name=os.getenv(
            "CHROMA_COLLECTION_NAME",
            "healthcare_documents",
        ),
        raw_data_dir=Path(os.getenv("RAW_DATA_DIR", PROJECT_ROOT / "data" / "raw")),
        processed_data_dir=Path(
            os.getenv("PROCESSED_DATA_DIR", PROJECT_ROOT / "data" / "processed")
        ),
        chroma_db_dir=Path(
            os.getenv("CHROMA_DB_DIR", PROJECT_ROOT / "data" / "vector_db" / "chroma")
        ),
        chunk_size=int(os.getenv("CHUNK_SIZE", "1000")),
        chunk_overlap=int(os.getenv("CHUNK_OVERLAP", "200")),
        retrieval_top_k=int(os.getenv("RETRIEVAL_TOP_K", "4")),
    )
