from pydantic import BaseModel

class BorrowCreate(BaseModel):

    member_id: int
    book_id: int