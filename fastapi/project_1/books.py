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



@app.get("/books/")
async def get_books_by_category(category: str):
    return [book for book in BOOKS if book["category"].casefold() == category.casefold()]

@app.get("/books/{book_author}")
async def read_books_author_category(author: str, category: str):
    return [book for book in BOOKS 
            if book["author"].casefold() == author.casefold()
            and book["category"].casefold() == category.casefold()]