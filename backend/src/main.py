import os
from contextlib import asynccontextmanager
from fastapi import FastAPI

from api.db import init_db, get_session
from api.chat.routing import router as chat_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield

app = FastAPI(lifespan=lifespan)
app.include_router(chat_router, prefix="/api/chats")


API_KEY = os.environ.get("API_KEY")
MY_PROJECT = os.environ.get("MY_PROJECT") or "This is my project"

if not API_KEY:
    raise NotImplementedError("'API_KEY' was not set")

@app.get("/")
def read_index():
    return {"hello": "world test", "project_name": MY_PROJECT}

@app.get("/healthz")
def health_check():
    return {"status": "ok"}

