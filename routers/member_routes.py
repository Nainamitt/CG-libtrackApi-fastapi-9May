from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import SessionLocal
from member import Member
from member_schema import MemberCreate

router = APIRouter()

# Database Dependency
def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


@router.post("/members")
def add_member(
    member: MemberCreate,
    db: Session = Depends(get_db)
):

    # Check duplicate email
    existing_member = db.query(Member).filter(
        Member.email == member.email
    ).first()

    if existing_member:

        return {
            "message": "Member already exists"
        }

    new_member = Member(
        name=member.name,
        email=member.email,
        course=member.course
    )

    db.add(new_member)
    db.commit()

    return {
        "message": "Member Added Successfully"
    }

@router.get("/members")
def get_members(db: Session = Depends(get_db)):

    members = db.query(Member).all()

    return members

from fastapi import HTTPException

# Update Member
@router.put("/members/{member_id}")
def update_member(
    member_id: int,
    updated_member: MemberCreate,
    db: Session = Depends(get_db)
):

    member = db.query(Member).filter(
        Member.id == member_id
    ).first()

    if not member:

        raise HTTPException(
            status_code=404,
            detail="Member Not Found"
        )

    member.name = updated_member.name
    member.email = updated_member.email
    member.course = updated_member.course

    db.commit()

    return {
        "message": "Member Updated Successfully"
    }

# Delete Member
@router.delete("/members/{member_id}")
def delete_member(
    member_id: int,
    db: Session = Depends(get_db)
):

    member = db.query(Member).filter(
        Member.id == member_id
    ).first()

    if not member:

        raise HTTPException(
            status_code=404,
            detail="Member Not Found"
        )

    db.delete(member)

    db.commit()

    return {
        "message": "Member Deleted Successfully"
    }

# Get Single Member
@router.get("/members/{member_id}")
def get_single_member(
    member_id: int,
    db: Session = Depends(get_db)
):

    member = db.query(Member).filter(
        Member.id == member_id
    ).first()

    if not member:

        raise HTTPException(
            status_code=404,
            detail="Member Not Found"
        )

    return member