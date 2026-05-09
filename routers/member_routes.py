from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
from models.member_model import Member
from schemas.member_schema import MemberCreate

router = APIRouter()


@router.post("/members")
def create_member(
    member: MemberCreate,
    db: Session = Depends(get_db)
):

    new_member = Member(
        name=member.name,
        email=member.email,
        course=member.course
    )

    db.add(new_member)
    db.commit()
    db.refresh(new_member)

    return {
        "message": "Member Created Successfully",
        "id": new_member.id
    }


@router.get("/members")
def get_members(
    db: Session = Depends(get_db)
):

    members = db.query(Member).all()

    return members


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
            detail="Member not found"
        )

    return member


@router.put("/members/{member_id}")
def update_member(
    member_id: int,
    member: MemberCreate,
    db: Session = Depends(get_db)
):

    existing_member = db.query(Member).filter(
        Member.id == member_id
    ).first()

    if not existing_member:

        raise HTTPException(
            status_code=404,
            detail="Member not found"
        )

    existing_member.name = member.name
    existing_member.email = member.email
    existing_member.course = member.course

    db.commit()

    return {
        "message": "Member Updated Successfully"
    }


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
            detail="Member not found"
        )

    db.delete(member)
    db.commit()

    return {
        "message": "Member Deleted Successfully"
    }