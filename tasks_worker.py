from celery import Celery
import os

from crewai import Crew, Process
from agents import financial_analyst
from task import analyze_financial_document
from database import save_analysis

celery_app = Celery(
    "worker",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0"
)

@celery_app.task
def run_analysis_task(query, filename, file_path):
    try:
        financial_crew = Crew(
            agents=[financial_analyst],
            tasks=[analyze_financial_document],
            process=Process.sequential,
        )

        result = financial_crew.kickoff({
            "query": query,
            "file_path": file_path
        })

        save_analysis(filename, query, str(result))

        return {"status": "completed", "result": str(result)}

    finally:
        if os.path.exists(file_path):
            os.remove(file_path)
