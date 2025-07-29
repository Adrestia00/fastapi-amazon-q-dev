from typing import List

from fastapi import APIRouter, HTTPException
from fastapi.param_functions import Depends

from fastapi_amazon_q_dev.db.dao.library_dao import AuthorDAO, BookDAO
from fastapi_amazon_q_dev.web.api.library.schema import (
    AuthorDTO,
    AuthorInputDTO,
    BookDTO,
    BookInputDTO,
)

router = APIRouter()


@router.post("/authors/", response_model=AuthorDTO)
async def create_author(
    author_data: AuthorInputDTO,
    author_dao: AuthorDAO = Depends(),
) -> AuthorDTO:
    """Create new author."""
    author = await author_dao.create_author(
        name=author_data.name,
        email=author_data.email,
    )
    return AuthorDTO.model_validate(author)


@router.get("/authors/", response_model=List[AuthorDTO])
async def get_authors(
    limit: int = 100,
    offset: int = 0,
    author_dao: AuthorDAO = Depends(),
) -> List[AuthorDTO]:
    """Get all authors."""
    authors = await author_dao.get_all_authors(limit=limit, offset=offset)
    return [AuthorDTO.model_validate(author) for author in authors]


@router.get("/authors/{author_id}", response_model=AuthorDTO)
async def get_author(
    author_id: int,
    author_dao: AuthorDAO = Depends(),
) -> AuthorDTO:
    """Get author by ID."""
    author = await author_dao.get_author_by_id(author_id)
    if not author:
        raise HTTPException(status_code=404, detail="Author not found")
    return AuthorDTO.model_validate(author)


@router.post("/books/", response_model=BookDTO)
async def create_book(
    book_data: BookInputDTO,
    book_dao: BookDAO = Depends(),
) -> BookDTO:
    """Create new book."""
    book = await book_dao.create_book(
        title=book_data.title,
        author_id=book_data.author_id,
        isbn=book_data.isbn,
    )

    new_book = await book_dao.get_book_by_id(book.id)
    return BookDTO.model_validate(new_book)


@router.get("/books/", response_model=List[BookDTO])
async def get_books(
    limit: int = 100,
    offset: int = 0,
    book_dao: BookDAO = Depends(),
) -> List[BookDTO]:
    """Get all books."""
    books = await book_dao.get_all_books(limit=limit, offset=offset)
    return [BookDTO.model_validate(book) for book in books]


@router.get("/books/{book_id}", response_model=BookDTO)
async def get_book(
    book_id: int,
    book_dao: BookDAO = Depends(),
) -> BookDTO:
    """Get book by ID."""
    book = await book_dao.get_book_by_id(book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return BookDTO.model_validate(book)


@router.get("/authors/{author_id}/books", response_model=List[BookDTO])
async def get_books_by_author(
    author_id: int,
    book_dao: BookDAO = Depends(),
) -> List[BookDTO]:
    """Get all books by author."""
    books = await book_dao.get_books_by_author(author_id)

    return [BookDTO.model_validate(book) for book in books]
