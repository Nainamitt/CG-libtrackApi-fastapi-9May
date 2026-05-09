from sqlalchemy import Column, Integer, String, DateTime
from database import Base
from sqlalchemy.sql import func

class Book(Base):

    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String, nullable=False)

    author = Column(String, nullable=False)

    isbn = Column(String, unique=True)

    category = Column(String)

    quantity = Column(Integer)

    available_quantity = Column(Integer)

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )