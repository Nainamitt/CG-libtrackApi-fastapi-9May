from fastapi import FastAPI

from database import Base, engine

from routers.book_routes import router as book_router
from routers.member_routes import router as member_router
from routers.borrow_routes import router as borrow_router

# Create Database Tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="LibTrack API Platform"
)

# Register Routers
app.include_router(book_router)

app.include_router(member_router)

app.include_router(borrow_router)


@app.get("/")
def home():

    return {
        "message": "LibTrack API Running Successfully"
    }