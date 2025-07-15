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

# @app.get("/books")
# async def read_all_books():
#     return BOOKS

# @app.get("/books/mybook")
# async def read_all_books():
#     return {'book_title': 'My favorite book!'}



# @app.get("/books/{book_title}")
# async def read_title(book_title: str):
#     for book in BOOKS:
#         if book['title'].casefold() == book_title.casefold():
#             return book
        

@app.get("/books/")
async def read_books_by_category(category: str):
    books_to_return = []
    for book in BOOKS:
        if book["category"].casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return

@app.get("/books/{book_author}")
async def read_category_by_query(book_author: str, category: str):
    books_to_return = []
    for book in BOOKS:
        if (
            book["author"].casefold() == book_author.casefold()
            and book["category"].casefold == category.casefold()
        ):
            books_to_return.append(book)
    return books_to_return
