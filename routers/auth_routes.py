from fastapi import APIRouter
from security import create_access_token

router = APIRouter()

@router.post("/login")
def login():

    token = create_access_token(
        {"sub": "admin"}
    )

    return {
        "access_token": token
    }