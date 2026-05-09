from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db

from models.book_model import Book
from models.member_model import Member
from models.borrow_model import Borrow

from schemas.borrow_schema import BorrowCreate

router = APIRouter()


@router.post("/borrow")
def borrow_book(
    data: BorrowCreate,
    db: Session = Depends(get_db)
):

    # Check Book
    book = db.query(Book).filter(
        Book.id == data.book_id
    ).first()

    if not book:

        raise HTTPException(
            status_code=404,
            detail="Book not found"
        )

    # Check Member
    member = db.query(Member).filter(
        Member.id == data.member_id
    ).first()

    if not member:

        raise HTTPException(
            status_code=404,
            detail="Member not found"
        )

    # Check Quantity
    if book.available_quantity <= 0:

        raise HTTPException(
            status_code=400,
            detail="Book not available"
        )

    # Create Borrow Record
    borrow = Borrow(
        member_id=data.member_id,
        book_id=data.book_id,
        status="Borrowed"
    )

    db.add(borrow)

    # Reduce quantity
    book.available_quantity -= 1

    db.commit()
    db.refresh(borrow)

    return {
        "message": "Book Borrowed Successfully",
        "borrow_id": borrow.id
    }


@router.put("/return/{borrow_id}")
def return_book(
    borrow_id: int,
    db: Session = Depends(get_db)
):

    borrow = db.query(Borrow).filter(
        Borrow.id == borrow_id
    ).first()

    if not borrow:

        raise HTTPException(
            status_code=404,
            detail="Borrow record not found"
        )

    if borrow.status == "Returned":

        raise HTTPException(
            status_code=400,
            detail="Book already returned"
        )

    borrow.status = "Returned"

    # Increase inventory
    book = db.query(Book).filter(
        Book.id == borrow.book_id
    ).first()

    if book:
        book.available_quantity += 1

    db.commit()

    return {
        "message": "Book Returned Successfully"
    }


@router.get("/borrow")
def get_borrow_records(
    db: Session = Depends(get_db)
):

    records = db.query(Borrow).all()

    return records