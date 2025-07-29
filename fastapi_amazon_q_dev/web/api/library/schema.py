from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict


class AuthorDTO(BaseModel):
    """DTO for author models."""
    
    id: int
    name: str
    email: Optional[str] = None
    
    model_config = ConfigDict(from_attributes=True)


class AuthorInputDTO(BaseModel):
    """DTO for creating new author."""
    
    name: str
    email: Optional[str] = None


class BookDTO(BaseModel):
    """DTO for book models."""
    
    id: int
    title: str
    isbn: Optional[str] = None
    description: Optional[str] = None
    published_date: Optional[datetime] = None
    author_id: int
    author: Optional[AuthorDTO] = None
    
    model_config = ConfigDict(from_attributes=True)


class BookInputDTO(BaseModel):
    """DTO for creating new book."""
    
    title: str
    author_id: int
    isbn: Optional[str] = None
    description: Optional[str] = None
    published_date: Optional[datetime] = None