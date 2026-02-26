from crewai import Agent, LLM
from tools import FinancialDocumentTool

llm = LLM(model="gpt-4o-mini", temperature=0.2)

financial_analyst = Agent(
    role="Senior Financial Analyst",
    goal="Provide accurate and evidence-based financial insights from the provided document.",
    backstory="You are an experienced financial analyst skilled in interpreting financial statements and reports.",
    verbose=True,
    memory=True,
    tools=[FinancialDocumentTool.read_data_tool],
    llm=llm,
)
