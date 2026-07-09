from fastapi import FastAPI
import logging

from app.api.health import router as health_router
from app.core.config import settings
from app.core.logging import setup_logging

setup_logging()

logger = logging.getLogger(__name__)

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
)

app.include_router(health_router)


@app.on_event("startup")
async def startup_event():
    logger.info("Starting Enterprise Intelligence OS...")


@app.get("/")
async def root():
    logger.info("Root endpoint accessed")

    return {
        "message": f"Welcome to {settings.APP_NAME}",
        "version": settings.APP_VERSION,
    }