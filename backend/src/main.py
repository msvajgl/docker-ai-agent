import os
from fastapi import FastAPI

API_KEY = os.environ.get("API_KEY")
MY_PROJECT = os.environ.get("MY_PROJECT") or "This is my project"

if not API_KEY:
    raise NotImplementedError("'API_KEY' was not set")

app = FastAPI()

@app.get("/")
def read_index():
    return {"hello": "world test", "project_name": MY_PROJECT}