# https://redeploy.udemy.com/course/fastapi-the-complete-course/learn/lecture/29025634#overview


from fastapi import FastAPI, HTTPException, Path
from pydantic import BaseModel, Field

app = FastAPI()

# ---------- Models ----------
# Define incoming request structure
class BookRequest(BaseModel):
    title: str = Field(min_length=3)
    author: str = Field(min_length=1)
    description: str = Field(min_length=1, max_length=100)
    rating: int = Field(ge=1, le=5)
    published_date: int

    model_config = {
        "json_schema_extra": {
            "example": {
                "title": "A new book",
                "author": "A new author",
                "description": "A new description",
                "rating": 5,
                "published_date": 2015
            }
        }
    }



# Define full book structure (includes ID)
class Book(BaseModel):
    id: int
    title: str
    author: str
    description: str
    rating: int
    published_date: int




# Fake stored book list (pretend these are from previous POSTs)
books = [
    Book(id=0, 
         title="Computer Science Pro", 
         author="Coding with Ruby",
         description="A very nice book", 
         rating=5, 
         published_date=2016),
    Book(id=1, 
         title="Be Fast with FastAPI", 
         author="Coding with RGB",
         description="A great book",
         rating=5, 
         published_date=2011),
]

def assign_id(book_data: dict) -> dict:
    # if books:
    #     book_data["id"] = books[-1].id + 1
    # else:
    #     book_data["id"] = 1
    # return book_data

    book_data["id"] = books[-1].id + 1 if books else 1
    return book_data




@app.get("/books")
async def read_all_books():
    return books


@app.get("/book/")
async def read_book_by_rating(book_rating: int):
    return [
        book for book in books if
        book.rating == book_rating
    ]

@app.get("/books/publish")
async def get_books_filter_by_date(date: int):
    return [
        book for book in books if
        book.published_date == date
    ]

@app.post("/create-book", response_model=Book, status_code=201)
async def create_book(book_request: BookRequest):
    book_data = book_request.model_dump(exclude_none=True)

    book_data = assign_id(book_data)

    new_book = Book(**book_data)
    books.append(new_book)
    return new_book



@app.get("/books/{book_id}")
async def read_book(book_id: int):
    for book in books:
        if book.id == book_id:
            return book
        


@app.put("/books/{book_id}", response_model=Book)
async def update_book(book_id: int, payload: BookRequest):
    for idx, stored in enumerate(books):
        if stored.id == book_id:
            updated = Book(id=book_id, **payload.model_dump())
            books[idx] = updated
            return updated
    raise HTTPException(status_code=404, detail="Book not found")


# path param

@app.delete("/books/{book_id}")
async def remove_book(book_id: int = Path(gt=0)):
    for idx, content in enumerate(books):
        if content.id == book_id:
            books.pop(idx)
            return

