from fastapi import FastAPI

app = FastAPI()

BOOKS = [
    {"title": "Title One", "author": "Author One", "category": "Science"},
    {"title": "Title Two", "author": "Author Two", "category": "Science"},
    {"title": "Title Three", "author": "Author Three", "category": "History"},
    {"title": "Title Four", "author": "Author Four", "category": "Math"},
    {"title": "Title Five", "author": "Author Five", "category": "Math"},
    {"title": "Title Six", "author": "Author Two", "category": "Math"},
]


@app.get("/books")
async def read_all_books():
    return BOOKS

@app.get("books/mybook")
async def read_all_books():
    return {'book_title': 'My favorite book!'}


@app.get("/books/{dynamic_param}")
async def read_all_books(dynamic_param: str):
    return {'dynamic_param': dynamic_param}
