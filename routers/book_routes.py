from fastapi import APIRouter, Depends, UploadFile, File
from sqlalchemy.orm import Session

from database import SessionLocal
from book import Book
from book_schema import BookCreate

from services.csv_service import upload_books

import shutil
import os

router = APIRouter()

# Database Dependency
def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


# Upload CSV
@router.post("/upload-books")
def upload_book_csv(
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):

    try:

        import os

        os.makedirs("uploads", exist_ok=True)

        file_path = f"uploads/{file.filename}"

        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        upload_books(file_path, db)

        return {
            "message": "CSV Uploaded Successfully"
        }

    except Exception as e:

        return {
            "error": str(e)
        }


# Add Book
@router.post("/books")
def add_book(
    book: BookCreate,
    db: Session = Depends(get_db)
):

    new_book = Book(
        title=book.title,
        author=book.author,
        isbn=book.isbn,
        category=book.category,
        quantity=book.quantity,
        available_quantity=book.quantity
    )

    db.add(new_book)
    db.commit()

    return {
        "message": "Book Added Successfully"
    }


# Get Books
@router.get("/books")
def get_books(db: Session = Depends(get_db)):

    books = db.query(Book).all()

    return books

from fastapi import HTTPException

# Update Book
@router.put("/books/{book_id}")
def update_book(
    book_id: int,
    updated_book: BookCreate,
    db: Session = Depends(get_db)
):

    book = db.query(Book).filter(
        Book.id == book_id
    ).first()

    # Check if book exists
    if not book:

        raise HTTPException(
            status_code=404,
            detail="Book Not Found"
        )

    # Update fields
    book.title = updated_book.title
    book.author = updated_book.author
    book.isbn = updated_book.isbn
    book.category = updated_book.category

    # Inventory update logic
    difference = updated_book.quantity - book.quantity

    book.quantity = updated_book.quantity

    book.available_quantity += difference

    db.commit()

    return {
        "message": "Book Updated Successfully"
    }

# Delete Book
@router.delete("/books/{book_id}")
def delete_book(
    book_id: int,
    db: Session = Depends(get_db)
):

    book = db.query(Book).filter(
        Book.id == book_id
    ).first()

    # Check existence
    if not book:

        raise HTTPException(
            status_code=404,
            detail="Book Not Found"
        )

    db.delete(book)

    db.commit()

    return {
        "message": "Book Deleted Successfully"
    }

# Get Single Book
@router.get("/books/{book_id}")
def get_single_book(
    book_id: int,
    db: Session = Depends(get_db)
):

    book = db.query(Book).filter(
        Book.id == book_id
    ).first()

    if not book:

        raise HTTPException(
            status_code=404,
            detail="Book Not Found"
        )

    return book

@router.put("/books/{book_id}")
def update_book(
    book_id: int,
    book: BookCreate,
    db: Session = Depends(get_db)
):

    existing_book = db.query(Book).filter(
        Book.id == book_id
    ).first()

    if not existing_book:
        return {"error": "Book not found"}

    existing_book.title = book.title
    existing_book.author = book.author
    existing_book.isbn = book.isbn
    existing_book.category = book.category
    existing_book.quantity = book.quantity
    existing_book.available_quantity = book.quantity

    db.commit()

    return {
        "message": "Book Updated Successfully"
    }

@router.delete("/books/{book_id}")
def delete_book(
    book_id: int,
    db: Session = Depends(get_db)
):

    book = db.query(Book).filter(
        Book.id == book_id
    ).first()

    if not book:
        return {"error": "Book not found"}

    db.delete(book)
    db.commit()

    return {
        "message": "Book Deleted Successfully"
    }