from pathlib import Path

from fastapi_amazon_q_dev.settings import settings


async def create_database() -> None:
    """Create a database."""


async def drop_database() -> None:
    """Drop current database."""
    if settings.db_file.exists():
        Path(settings.db_file).unlink()
