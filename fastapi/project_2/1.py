from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

# --- Models ---

# Model for incoming data (used in POST request)
class BookRequest(BaseModel):
    id: Optional[int] = None  # Client doesn't supply this
    title: str = Field(min_length=3)
    author: str = Field(min_length=1)
    description: str = Field(min_length=1, max_length=100)
    rating: int = Field(ge=1, le=5)

# Model for internal use and storage
class Book(BaseModel):
    id: int
    title: str
    author: str
    description: str
    rating: int

# --- In-memory storage ---

books = [
    Book(id=1, title="Computer Science Pro", author="Coding with Ruby", description="A very nice book", rating=5),
    Book(id=2, title="Be Fast with FastAPI", author="Coding with RGB", description="A great book", rating=5),
    Book(id=3, title="Master Endpoints", author="Coding with Robi", description="An awesome book", rating=5),
    Book(id=4, title="HP1", author="Author 1", description="Book description", rating=2),
    Book(id=5, title="HP2", author="Author 2", description="Book description", rating=3),
    Book(id=6, title="HP3", author="Author 3", description="Book description", rating=1),
]

# --- Utility ---

def find_book_id(book: Book):
    last_book = books[-1] if books else None
    book.id = last_book.id + 1 if last_book and last_book.id is not None else 1

# --- Routes ---

@app.post("/create-book")
async def create_book(book_request: BookRequest):
    new_book = Book(**book_request.model_dump())
    find_book_id(new_book)
    books.append(new_book)
