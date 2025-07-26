


from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field, ConfigDict

app = FastAPI()

class BookRequest(BaseModel):
    title: str = Field(min_length=3)
    author: str = Field(min_length=1)
    description: str = Field(min_length=1, max_length=100)
    rating: int = Field(ge=1, le=5)
    
    model_config = {
        "json_schema_extra": {
            "example": {
                "title": "a new book",
                "author": "a new author",
                "description": "a new description",
                "rating": 5
            }
        }
    }

class Book(BaseModel):
    id: int
    title: str
    author: str
    description: str
    rating: int

books = [
    Book(id=1, title="Computer Science Pro", author="Coding with Ruby",
         description="A very nice book", rating=5),
    Book(id=2, title="Be Fast with FastAPI", author="Coding with RGB",
         description="A great book", rating=5),
]

def add_id(book_data: dict) -> dict:
    book_data["id"] = books[-1].id + 1 if books else 1
    return book_data


@app.put("/books/{id}", response_model=Book)
async def update_book(book_id:int, payload: BookRequest):
    for idx, content in enumerate(books):
        if content.id == book_id:
            updated = Book(id=book_id, **payload.model_dump())
            books[idx] = updated
            return updated