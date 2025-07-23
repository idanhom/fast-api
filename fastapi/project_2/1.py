from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

# ---------- Models ----------
class BookRequest(BaseModel):                 # data sent by the client
    id: Optional[int] = None
    title: str = Field(min_length=3)
    author: str = Field(min_length=1)
    description: str = Field(min_length=1, max_length=100)
    rating: int = Field(ge=1, le=5)

class Book(BaseModel):                        # data stored by the server
    id: int
    title: str
    author: str
    description: str
    rating: int

# ---------- In-memory storage ----------
books = [
    Book(id=1, title="Computer Science Pro", author="Coding with Ruby",
         description="A very nice book", rating=5),
    Book(id=2, title="Be Fast with FastAPI", author="Coding with RGB",
         description="A great book", rating=5),
]

# ---------- Helper ----------
def find_book_id(book: Book) -> None:
    last_book = books[-1] if books else None
    
    book.id = last_book.id + 1 if last_book and last_book.id is not None else 1

# ---------- Route ----------
@app.post("/create-book")
async def create_book(book_request: BookRequest):
    new_book = Book(**book_request.model_dump())  # convert validated input → Book
    find_book_id(new_book)                        # assign missing id
    books.append(new_book)                        # store in list