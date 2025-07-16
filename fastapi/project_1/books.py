from fastapi import FastAPI

app = FastAPI()

BOOKS = [
    {"title": "Title One", "author": "Author One", "category": "Science"},
    {"title": "Title Two", "author": "Author Two", "category": "Science"},
    {"title": "Title Three", "author": "Author Three", "category": "History"},
    {"title": "Title Four", "author": "Author Four", "category": "Math"},
    {"title": "Title Five", "author": "Author Five", "category": "Math"},
    {"title": "Title Six", "author": "Author Two", "category": "Math"},
    {"title": "Title Seven", "author": "Author Two", "category": "Science"},
]

# ### 1. **Return All Books in a Specific Category and by a Specific Author**

# **Endpoint Design**: Combine path and query parameters.
# **Goal**: Fetch books where both the author and category match.
# @app.get("/books/{author}")
# async def get_book_by_author_category(author: str, category: str):
#     return [
#         book for book in BOOKS if
#         book["author"].casefold() == author.casefold()
#         and book["category"].casefold() == category.casefold()
#     ]











# ---

# ### 2. **Return a List of Unique Categories**

# **Endpoint Design**: Use a simple path (e.g., `/categories`).
# **Goal**: Extract and return a list of all unique book categories.

# @app.get("/books/categories/")
# async def unique_categories():
#     return {
#         book["category"] for book in BOOKS
#     }



















# ---

# ### 3. **Return the First Book Matching a Partial Title Match**

# **Endpoint Design**: Use a query parameter like `?search=some_word`.
# **Goal**: Find and return the **first book** where the title contains the keyword.
# @app.get("/books/search/")
# async def search(keyword: str):
#     for book in BOOKS:
#         if keyword.casefold() in book["title"].casefold():
#             return book
























# @app.get("/books/search/")
# async def return_first(search: str):
#     for book in BOOKS:
#         if search.casefold() in book["title"].casefold():
#             return book






# ---

# ### 4. **Return Whether a Book Exists Based on Title**

# **Endpoint Design**: Use a query parameter for the title.
# **Goal**: Return `{"exists": True}` or `{"exists": False}` depending on whether a book with the given title exists.
# @app.get("/books/result/")
# async def is_existing(title: str):
#     for book in BOOKS:
#         if book["title"].casefold() == title.casefold():
#             return {"exists": True}
#     return {"exists": False}















# ---

# ### 5. **Return All Books Sorted Alphabetically by Title**

# **Endpoint Design**: Simple path endpoint (e.g., `/books/sorted`).
# **Goal**: Return all books sorted by their title in ascending order.
# @app.get("/books/sorted/")
# async def sorted_alpha():
#     return sorted(set(book["title"] for book in BOOKS))



# ---

# 6 Return the Number of Books in Each Category
# Endpoint design: simple path /categories/counts
# Goal: Respond with a dictionary where each key is a category and each value is the count of books in that category, e.g.

# json
# Copy
# Edit
# {"Science": 3, "Math": 3, "History": 1}
# Bloom cues: Understand how to aggregate; Apply a loop or collections.Counter; Analyse readability vs. performance.

# @app.get("/categories/counts")
# async def count_books_per_category():
#     # ❶ Pull every category into a list (list-comprehension)
#     categories = [book["category"] for book in BOOKS]

#     # ❷ Dict-comprehension:
#     #    - set(categories)  ➜ unique category names
#     #    - categories.count(cat) loops inside Python’s built-in .count()
#     return {cat: categories.count(cat) for cat in set(categories)}
