from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base

class Borrow(Base):

    __tablename__ = "borrow_records"

    id = Column(Integer, primary_key=True)

    member_id = Column(Integer, ForeignKey("members.id"))

    book_id = Column(Integer, ForeignKey("books.id"))

    status = Column(String, default="Borrowed")