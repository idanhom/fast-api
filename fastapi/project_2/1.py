from fastapi import FastAPI
from pydantic import BaseModel, Field


app = FastAPI()

class Book(BaseModel):
    id: int
    title: str = Field(min_length=1)
    author: str = Field(min_length=1)
    description: str = Field(min_length=1)
    rating: int = Field(ge=1, le=5)


books = [
    Book(id=1, 
         title="Computer Science Pro", 
         author="Coding with Ruby", 
         description="A very nice book", 
         rating=5),
    Book(id=2, 
         title="Be Fast with FastAPI", 
         author="Coding with RGB", 
         description="A great book", 
         rating=5),
    Book(id=3, 
         title="Master Endpoints", 
         author="Coding with Robi", 
         description="An awesome book", 
         rating=5),
    Book(id=4, 
         title="HP1", 
         author="Author 1", 
         description="Book description", 
         rating=2),
    Book(id=5, 
         title="HP2", 
         author="Author 2", 
         description="Book description", 
         rating=3),
    Book(id=6, 
         title="HP3", 
         author="Author 3", 
         description="Book description", 
         rating=1)
]

@app.post("/create-book")
async def create_book(book_request: Book):
    new_book = Book(**book_request.model_dump())
    books.append(new_book)
    
@app.get("/books")
async def view_books():
    return books