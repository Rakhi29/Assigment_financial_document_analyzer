from crewai import Task
from agents import financial_analyst
from tools import FinancialDocumentTool

analyze_financial_document = Task(
    description="""Analyze the financial document at {file_path}.

User Query:
{query}
""",
    expected_output="""Structured financial analysis including:

- Executive Summary
- Financial Highlights
- Risk Factors
- Insights
""",
    agent=financial_analyst,
    tools=[FinancialDocumentTool.read_data_tool],
)
