from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import json
import os

app = FastAPI()

# Allow all origins (CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load marks from file (once at startup)
with open("marks.json", "r") as f:
    student_marks = json.load(f)

@app.get("/api")
async def get_marks(request: Request):
    names = request.query_params.getlist("name")
    marks = [student_marks.get(name, None) for name in names]
    return {"marks": marks}
