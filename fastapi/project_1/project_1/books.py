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

# ### 1. **Return All Books in a Specific Category and by a Specific Author**

# **Endpoint Design**: Combine path and query parameters.
# **Goal**: Fetch books where both the author and category match.

@app.get("/books/{author}")
async def get_books_by_author_category(author: str, category: str):
    return [
        book for book in BOOKS if
        book["author"].casefold() == author.casefold()
        and book["category"].casefold() == category.casefold()
    ]























# @app.get("/books/{author}")
# async def read_book_by_author_category(author: str, category: str):
#     return [
#         book for book in BOOKS if
#             book["author"].casefold() == author.casefold() 
#             and book["category"].casefold() == category.casefold()
#             ]

# ---

# ### 2. **Return a List of Unique Categories**

# **Endpoint Design**: Use a simple path (e.g., `/categories`).
# **Goal**: Extract and return a list of all unique book categories.

# ---

# ### 3. **Return the First Book Matching a Partial Title Match**

# **Endpoint Design**: Use a query parameter like `?search=some_word`.
# **Goal**: Find and return the **first book** where the title contains the keyword.

# ---

# ### 4. **Return Whether a Book Exists Based on Title**

# **Endpoint Design**: Use a query parameter for the title.
# **Goal**: Return `{"exists": True}` or `{"exists": False}` depending on whether a book with the given title exists.

# ---

# ### 5. **Return All Books Sorted Alphabetically by Title**

# **Endpoint Design**: Simple path endpoint (e.g., `/books/sorted`).
# **Goal**: Return all books sorted by their title in ascending order.

# ---

