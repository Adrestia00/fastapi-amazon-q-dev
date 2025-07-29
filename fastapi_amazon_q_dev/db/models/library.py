from datetime import datetime
from typing import Optional

from sqlalchemy import ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql.sqltypes import String, DateTime

from fastapi_amazon_q_dev.db.base import Base


class Author(Base):
    """Author model."""

    __tablename__ = "authors"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(length=200))
    email: Mapped[Optional[str]] = mapped_column(String(length=255), nullable=True)
    
    books: Mapped[list["Book"]] = relationship("Book", back_populates="author")


class Book(Base):
    """Book model."""

    __tablename__ = "books"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String(length=300))
    isbn: Mapped[Optional[str]] = mapped_column(String(length=20), nullable=True, unique=True)
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    published_date: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)
    author_id: Mapped[int] = mapped_column(ForeignKey("authors.id"))
    
    author: Mapped["Author"] = relationship("Author", back_populates="books")