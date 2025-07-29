from typing import List, Optional

from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from fastapi_amazon_q_dev.db.dependencies import get_db_session
from fastapi_amazon_q_dev.db.models.library import Author, Book


class AuthorDAO:
    """Class for accessing authors table."""

    def __init__(self, session: AsyncSession = Depends(get_db_session)) -> None:
        self.session = session

    async def create_author(self, name: str, email: Optional[str] = None) -> Author:
        """Create new author."""
        author = Author(name=name, email=email)
        self.session.add(author)
        await self.session.flush()
        return author

    async def get_all_authors(self, limit: int = 100, offset: int = 0) -> List[Author]:
        """Get all authors with pagination."""
        result = await self.session.execute(select(Author).limit(limit).offset(offset))
        return list(result.scalars().fetchall())

    async def get_author_by_id(self, author_id: int) -> Optional[Author]:
        """Get author by ID with books."""
        result = await self.session.execute(
            select(Author)
            .options(selectinload(Author.books))
            .where(Author.id == author_id)
        )
        return result.scalar_one_or_none()


class BookDAO:
    """Class for accessing books table."""

    def __init__(self, session: AsyncSession = Depends(get_db_session)) -> None:
        self.session = session

    async def create_book(
        self, title: str, author_id: int, isbn: Optional[str] = None
    ) -> Book:
        """Create new book."""
        book = Book(title=title, author_id=author_id, isbn=isbn)
        self.session.add(book)
        await self.session.flush()
        return book

    async def get_all_books(self, limit: int = 100, offset: int = 0) -> List[Book]:
        """Get all books with authors."""
        result = await self.session.execute(
            select(Book).options(selectinload(Book.author)).limit(limit).offset(offset)
        )
        return list(result.scalars().fetchall())

    async def get_book_by_id(self, book_id: int) -> Optional[Book]:
        """Get book by ID with author."""
        result = await self.session.execute(
            select(Book).options(selectinload(Book.author)).where(Book.id == book_id)
        )
        return result.scalar_one_or_none()

    async def get_books_by_author(self, author_id: int) -> List[Book]:
        """Get all books by author."""
        result = await self.session.execute(
            select(Book)
            .options(selectinload(Book.author))
            .where(Book.author_id == author_id)
        )
        return list(result.scalars().fetchall())
