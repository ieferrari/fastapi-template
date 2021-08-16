"""Template for FastAPI applications."""
from fastapi import FastAPI


app = FastAPI(title="FastAPI template App",
              description="Template for generic FastAPI project",
              version="0.1.0",
              )


@app.get("/")
async def root():
    return {"msg": "Hello FastAPI-template!"}
