"""Template for FastAPI applications."""
from fastapi import FastAPI
from routers import front, users, items
from fastapi.staticfiles import StaticFiles
from db.database import  Base, engine

app = FastAPI(title="FastAPI Template App",
              description="Template for generic FastAPI project",
              version="0.1.0",
              )

app.include_router(front.router)
app.include_router(users.router, prefix='/u', tags=["users"])
app.include_router(items.router, prefix='/i', tags=["items"])
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/ping")
async def root():
    return {"msg": "Hello FastAPI-template!"}

Base.metadata.create_all(bind=engine)
