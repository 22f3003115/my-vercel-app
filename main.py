from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

# Allow all origins (CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load and transform marks data into a dictionary
with open("marks.json", "r") as f:
    marks_list = json.load(f)
    student_marks = {entry["name"]: entry["marks"] for entry in marks_list}

@app.get("/api")
async def get_marks(request: Request):
    names = request.query_params.getlist("name")
    marks = [student_marks.get(name, None) for name in names]
    return {"marks": marks}
