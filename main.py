from fastapi import FastAPI
from database import engine, Base

from routers import (
    book_routes,
    member_routes,
    borrow_routes,
    auth_routes,
    analytics_routes
)

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="LibTrack API",
    description="Smart Library Management System",
    version="1.0"
)

app.include_router(book_routes.router)
app.include_router(member_routes.router)
app.include_router(borrow_routes.router)
app.include_router(auth_routes.router)
app.include_router(analytics_routes.router)