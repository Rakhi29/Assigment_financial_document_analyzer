from dotenv import load_dotenv
load_dotenv()

from langchain_community.document_loaders import PyPDFLoader

class FinancialDocumentTool:
    @staticmethod
    def read_data_tool(path: str):
        docs = PyPDFLoader(file_path=path).load()

        full_report = ""
        for data in docs:
            content = data.page_content
            while "\n\n" in content:
                content = content.replace("\n\n", "\n")
            full_report += content + "\n"

        return full_report
