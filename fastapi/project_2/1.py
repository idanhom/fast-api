# https://redeploy.udemy.com/course/fastapi-the-complete-course/learn/lecture/29025634#overview


from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

# ---------- Models ----------
# Define incoming request structure
class BookRequest(BaseModel):
    id: Optional[int] = Field(description='ID is not needed on create', default=None)
    title: str = Field(min_length=3)
    author: str = Field(min_length=1)
    description: str = Field(min_length=1, max_length=100)
    rating: int = Field(ge=1, le=5)

    model_config = {
        "json_schema_extra": {
            "example": {
                "title": "A new book",
                "author": "A new author",
                "description": "A new description",
                "rating": 5
            }
        }
    }

# 

# Define full book structure (includes ID)
class Book(BaseModel):
    id: int
    title: str
    author: str
    description: str
    rating: int

# Fake stored book list (pretend these are from previous POSTs)
books = [
    Book(id=1, title="Computer Science Pro", author="Coding with Ruby",
         description="A very nice book", rating=5),
    Book(id=2, title="Be Fast with FastAPI", author="Coding with RGB",
         description="A great book", rating=5),
]

def assign_id(book_data: dict) -> dict:
    # if books:
    #     book_data["id"] = books[-1].id + 1
    # else:
    #     book_data["id"] = 1
    # return book_data


    book_data["id"] = books[-1].id + 1 if books else 1
    return book_data










# ---------- Route ----------
@app.post("/create-book", response_model=Book, status_code=201)
async def create_book(book_request: BookRequest):
    book_data = book_request.model_dump(exclude_none=True)

    book_data = assign_id(book_data)

    # # Assign id ourselves
    # if books:
    #     book_data["id"] = books[-1].id + 1
    # else:
    #     book_data["id"] = 1

    new_book = Book(**book_data)
    books.append(new_book)
    return new_book

