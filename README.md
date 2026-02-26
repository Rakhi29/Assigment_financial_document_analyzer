# Financial Document Analyzer – Enhanced Version

## Overview
This version extends the base analyzer with:

- Queue Worker Model using Celery and Redis for concurrent request handling
- SQLite database integration for persistent storage of analysis results

---

## Queue Worker Model

Celery is used to offload document analysis into background workers.

### Start Redis
redis-server

### Start Celery Worker
celery -A tasks_worker.celery_app worker --loglevel=info

---

## Database Integration

SQLite database (`analysis.db`) stores:

- Filename
- Query
- Analysis Result
- Timestamp

---

## Setup

pip install -r requirements.txt

Set environment variables:

export OPENAI_API_KEY=your_api_key_here

---

## Run API

uvicorn main:app --reload

---

## Usage

POST /analyze

Response:

{
  "status": "queued",
  "task_id": "<celery_task_id>"
}

---

## Architecture

Client → FastAPI → Celery Queue → Worker → CrewAI → SQLite
