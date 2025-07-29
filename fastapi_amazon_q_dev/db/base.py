from sqlalchemy.orm import DeclarativeBase

from fastapi_amazon_q_dev.db.meta import meta


class Base(DeclarativeBase):
    """Base for all models."""

    metadata = meta
