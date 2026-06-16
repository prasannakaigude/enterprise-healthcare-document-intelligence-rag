"""Health check logic for the backend application."""

from pathlib import Path
from typing import Dict

from backend.app.core.settings import Settings, get_settings


def _path_status(path: Path) -> Dict[str, object]:
    """Return a simple status dictionary for a required local path."""

    return {
        "path": str(path),
        "exists": path.exists(),
    }


def get_health_status(settings: Settings = None) -> Dict[str, object]:
    """Return basic project health information.

    This does not call OpenAI, ChromaDB, FastAPI, or AWS. It only confirms that
    the local Python project foundation can load settings and see key folders.
    """

    active_settings = settings or get_settings()

    return {
        "status": "ok",
        "app_name": active_settings.app_name,
        "app_version": active_settings.app_version,
        "environment": active_settings.environment,
        "paths": {
            "raw_data_dir": _path_status(active_settings.raw_data_dir),
            "processed_data_dir": _path_status(active_settings.processed_data_dir),
            "chroma_db_dir": _path_status(active_settings.chroma_db_dir),
        },
    }
