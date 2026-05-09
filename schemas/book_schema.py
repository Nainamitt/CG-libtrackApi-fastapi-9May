from pydantic import BaseModel, Field

class BookCreate(BaseModel):

    title: str = Field(
        min_length=2,
        max_length=100
    )

    author: str

    isbn: str

    category: str

    quantity: int = Field(gt=0)