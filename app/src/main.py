import os

from fastapi import FastAPI
from .db.database import RDSClientBase

app = FastAPI()

# models.Base.metadata.create_all(engine)


@app.on_event("startup")
async def start_db():
    RDSClientBase()


@app.get("/")
async def root():
    return {"result": "success"}
