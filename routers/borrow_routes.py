from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import SessionLocal
from borrow import Borrow
from book import Book
from borrow_schema import BorrowCreate

router = APIRouter()

def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()

# Borrow Book
@router.post("/borrow")
def borrow_book(
    data: BorrowCreate,
    db: Session = Depends(get_db)
):

    book = db.query(Book).filter(
        Book.id == data.book_id
    ).first()

    if book.available_quantity <= 0:

        return {
            "message": "Book Not Available"
        }

    borrow = Borrow(
        member_id=data.member_id,
        book_id=data.book_id
    )

    book.available_quantity -= 1

    db.add(borrow)

    db.commit()

    return {
        "message": "Book Borrowed"
    }

# Return Book
@router.put("/return/{borrow_id}")
def return_book(
    borrow_id: int,
    db: Session = Depends(get_db)
):

    borrow = db.query(Borrow).filter(
        Borrow.id == borrow_id
    ).first()

    borrow.status = "Returned"

    book = db.query(Book).filter(
        Book.id == borrow.book_id
    ).first()

    book.available_quantity += 1

    db.commit()

    return {
        "message": "Book Returned"
    }