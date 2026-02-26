from fastapi import FastAPI, File, UploadFile, Form, HTTPException
import os
import uuid

from tasks_worker import run_analysis_task
from database import init_db

app = FastAPI(title="Financial Document Analyzer")

init_db()

@app.get("/")
async def root():
    return {"message": "Financial Document Analyzer API is running"}

@app.post("/analyze")
async def analyze(
    file: UploadFile = File(...),
    query: str = Form(default="Analyze this financial document")
):
    file_id = str(uuid.uuid4())
    file_path = f"data/{file_id}.pdf"

    try:
        os.makedirs("data", exist_ok=True)

        with open(file_path, "wb") as f:
            f.write(await file.read())

        task = run_analysis_task.delay(query.strip(), file.filename, file_path)

        return {
            "status": "queued",
            "task_id": task.id
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
