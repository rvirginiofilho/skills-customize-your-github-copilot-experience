"""Starter code for Building REST APIs with FastAPI assignment."""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title="Books API")


class BookInput(BaseModel):
    title: str = Field(min_length=1, max_length=120)
    author: str = Field(min_length=1, max_length=80)
    year: int = Field(ge=1500, le=2100)


class Book(BookInput):
    id: int


# In-memory store for practice purposes.
books: list[Book] = []
next_id = 1


@app.get("/health")
def health_check() -> dict[str, str]:
    """Return API status."""
    return {"status": "ok"}


@app.get("/books")
def list_books() -> list[Book]:
    """Return all books."""
    # TODO: Return all books from the in-memory store.
    raise NotImplementedError


@app.get("/books/{book_id}")
def get_book(book_id: int) -> Book:
    """Return one book by ID."""
    # TODO: Find and return the matching book.
    # Raise HTTPException(status_code=404, detail="Book not found") if missing.
    raise NotImplementedError


@app.post("/books", status_code=201)
def create_book(payload: BookInput) -> Book:
    """Create and return a new book."""
    # TODO: Use next_id, append to books list, and return the created book.
    raise NotImplementedError


@app.put("/books/{book_id}")
def update_book(book_id: int, payload: BookInput) -> Book:
    """Update an existing book by ID."""
    # TODO: Replace the book data and return updated value.
    # Raise HTTPException(status_code=404, detail="Book not found") if missing.
    raise NotImplementedError


@app.delete("/books/{book_id}")
def delete_book(book_id: int) -> dict[str, str]:
    """Delete a book and return confirmation message."""
    # TODO: Remove matching book.
    # Raise HTTPException(status_code=404, detail="Book not found") if missing.
    raise NotImplementedError
