from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
from models.book_model import Book
from schemas.book_schema import BookCreate

router = APIRouter()


@router.post("/books")
def create_book(
    book: BookCreate,
    db: Session = Depends(get_db)
):

    new_book = Book(
        title=book.title,
        author=book.author,
        isbn=book.isbn,
        category=book.category,
        available_quantity=book.quantity
    )

    db.add(new_book)
    db.commit()
    db.refresh(new_book)

    return {
        "message": "Book Created Successfully",
        "id": new_book.id
    }


@router.get("/books")
def get_books(
    db: Session = Depends(get_db)
):

    books = db.query(Book).all()

    return books


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
            detail="Book not found"
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

        raise HTTPException(
            status_code=404,
            detail="Book not found"
        )

    existing_book.title = book.title
    existing_book.author = book.author
    existing_book.isbn = book.isbn
    existing_book.category = book.category
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

        raise HTTPException(
            status_code=404,
            detail="Book not found"
        )

    db.delete(book)
    db.commit()

    return {
        "message": "Book Deleted Successfully"
    }