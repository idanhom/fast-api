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


# ---------- Route ----------
@app.post("/create-book", response_model=Book, status_code=201)
async def create_book(book_request: BookRequest):
    book_data = book_request.model_dump(exclude_none=True)

    # Assign id ourselves
    if books:
        book_data["id"] = books[-1].id + 1
    else:
        book_data["id"] = 1

    new_book = Book(**book_data)
    books.append(new_book)
    return new_book
