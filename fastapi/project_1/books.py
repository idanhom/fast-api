from fastapi import FastAPI

app = FastAPI()

BOOKS = [
    {"title": "Title One", "author": "Author One", "category": "Science"},
    {"title": "Title Two", "author": "Author Two", "category": "History"},
    {"title": "Title Three", "author": "Author Three", "category": "Math"},
    {"title": "Title Four", "author": "Author Four", "category": "Science"},
    {"title": "Title Five", "author": "Author Five", "category": "History"},
]


@app.get("/books")
async def read_all_book():
    return BOOKS
