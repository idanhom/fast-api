from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel

app = FastAPI()

BOOKS = [
    {"title": "Title One", "author": "Author One", "category": "Science"},
    {"title": "Title Two", "author": "Author Two", "category": "Science"},
    {"title": "Title Three", "author": "Author Three", "category": "History"},
    {"title": "Title Four", "author": "Author Four", "category": "Math"},
    {"title": "Title Five", "author": "Author Five", "category": "Math"},
    {"title": "Title Six", "author": "Author Two", "category": "Math"},
]

class Book(BaseModel):
    title: str
    author: str
    category: str

@app.post("/books", status_code=status.HTTP_201_CREATED)
async def create_book(book: Book):
    BOOKS.append(book.model_dump())
    























# from pydantic import BaseModel

# class Book(BaseModel):
#     title: str
#     author: str
#     category: str

# @app.post("/books/create")
# async def create_book(new_book: Book):
#     BOOKS.append(new_book.dict())
#     return new_book