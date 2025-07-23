from pydantic import BaseModel, Field
from typing import Optional

# Define incoming request structure
class BookRequest(BaseModel):
    id: Optional[int] = None
    title: str
    author: str
    description: str
    rating: int

# Define full book structure (includes ID)
class Book(BaseModel):
    id: int
    title: str
    author: str
    description: str
    rating: int

# Fake stored book list (pretend these are from previous POSTs)
books = [
    Book(id=1, title="Book 1", author="A", description="...", rating=5),
    Book(id=2, title="Book 2", author="B", description="...", rating=4),
]

# Imagine this is what the client sends
client_input = BookRequest(
    title="New Book",
    author="New Author",
    description="New Description",
    rating=5
)

# 🔍 1. Convert incoming object to dict
book_data = client_input.model_dump(exclude_none=True)
print("📤 Incoming data →", book_data)

# 🔍 2. Add a unique ID from the existing books
if books:
    book_data["id"] = books[-1].id + 1
else:
    book_data["id"] = 1
print("📎 After adding ID →", book_data)

# ✅ 3. Make a full Book object and add to storage
new_book = Book(**book_data)
books.append(new_book)
print("📚 Final book list →", books)
