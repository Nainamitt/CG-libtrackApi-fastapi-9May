from pydantic import BaseModel

class MemberCreate(BaseModel):

    name: str
    email: str
    course: str