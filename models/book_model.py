from sqlalchemy import Column, Integer, String

from database import Base


class Book(Base):

    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String)

    author = Column(String)

    isbn = Column(String)

    category = Column(String)

    available_quantity = Column(Integer)