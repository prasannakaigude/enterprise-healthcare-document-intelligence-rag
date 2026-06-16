"""FastAPI application entrypoint."""

from fastapi import FastAPI

from backend.app.api.routes import router
from backend.app.core.settings import get_settings


settings = get_settings()

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
)
app.include_router(router)

