from sqlalchemy import Column, Integer, String

from database import Base


class Borrow(Base):

    __tablename__ = "borrow_records"

    id = Column(Integer, primary_key=True, index=True)

    member_id = Column(Integer)

    book_id = Column(Integer)

    status = Column(String)