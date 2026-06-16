"""Small client for calling the FastAPI backend from Streamlit."""

from typing import Any, Dict, List, Optional
import os
import warnings

warnings.filterwarnings("ignore", message="urllib3 v2 only supports OpenSSL.*")
import requests


DEFAULT_BACKEND_URL = os.getenv("BACKEND_URL", "http://127.0.0.1:8000")


class BackendAPIError(Exception):
    """Raised when the backend API cannot return a usable response."""


def ask_backend(
    question: str,
    backend_url: str = DEFAULT_BACKEND_URL,
    file_name: Optional[str] = None,
) -> Dict[str, Any]:
    """Send a question to the FastAPI backend."""

    cleaned_question = question.strip()

    if not cleaned_question:
        raise ValueError("question cannot be empty")

    try:
        response = requests.post(
            f"{backend_url.rstrip('/')}/ask",
            json={"question": cleaned_question, "file_name": file_name},
            timeout=30,
        )
    except requests.RequestException as error:
        raise BackendAPIError(
            "Could not connect to the FastAPI backend. Start it with "
            "`python3 scripts/run_api.py` and try again."
        ) from error

    if response.status_code != 200:
        try:
            detail = response.json().get("detail", response.text)
        except ValueError:
            detail = response.text
        raise BackendAPIError(f"Backend returned {response.status_code}: {detail}")

    return response.json()


def list_documents_backend(
    backend_url: str = DEFAULT_BACKEND_URL,
) -> List[Dict[str, Any]]:
    """Fetch selectable documents from the FastAPI backend."""

    try:
        response = requests.get(
            f"{backend_url.rstrip('/')}/documents",
            timeout=30,
        )
    except requests.RequestException as error:
        raise BackendAPIError(
            "Could not connect to the FastAPI backend. Start it with "
            "`python3 scripts/run_api.py` and try again."
        ) from error

    if response.status_code != 200:
        try:
            detail = response.json().get("detail", response.text)
        except ValueError:
            detail = response.text
        raise BackendAPIError(f"Backend returned {response.status_code}: {detail}")

    return response.json()


def rebuild_vector_store_backend(
    backend_url: str = DEFAULT_BACKEND_URL,
) -> Dict[str, Any]:
    """Ask the FastAPI backend to rebuild the vector store."""

    try:
        response = requests.post(
            f"{backend_url.rstrip('/')}/ingest/rebuild",
            timeout=300,
        )
    except requests.RequestException as error:
        raise BackendAPIError(
            "Could not connect to the FastAPI backend. Start it with "
            "`python3 scripts/run_api.py` and try again."
        ) from error

    if response.status_code != 200:
        try:
            detail = response.json().get("detail", response.text)
        except ValueError:
            detail = response.text
        raise BackendAPIError(f"Backend returned {response.status_code}: {detail}")

    return response.json()
