from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import SessionLocal
from book import Book
from borrow import Borrow

router = APIRouter()

def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()

@router.get("/analytics")
def analytics(db: Session = Depends(get_db)):

    total_books = db.query(Book).count()

    borrowed_books = db.query(Borrow).filter(
        Borrow.status == "Borrowed"
    ).count()

    returned_books = db.query(Borrow).filter(
        Borrow.status == "Returned"
    ).count()

    return {
        "total_books": total_books,
        "borrowed_books": borrowed_books,
        "returned_books": returned_books
    }