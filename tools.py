from dotenv import load_dotenv
load_dotenv()
import os
import json
from langchain.tools import BaseTool
from langchain_community.utilities import GoogleSerperAPIWrapper

class InternetSearchTool(BaseTool):
    name = "Search the internet"
    description = "A tool that can be used to search the internet with a search query."

    def _run(self, query: str):
        search = GoogleSerperAPIWrapper(serper_api_key=os.getenv('SERPER_API_KEY'))
        results = search.results(query)
        return json.dumps(results, ensure_ascii=False, indent=2)

    def _arun(self, query: str):
        raise NotImplementedError("This tool does not support async")

class QueryEmployeeDataTool(BaseTool):
    name = "Query Employee Data"
    description = "Use this to query employee data by employee ID."

    def _run(self, employee_id: str):
        return f"Employee data for ID {employee_id}"

    def _arun(self, employee_id: str):
        raise NotImplementedError("This tool does not support async")

class UpdateEmployeeRecordTool(BaseTool):
    name = "Update Employee Record"
    description = "Use this to update an employee's record."

    def _run(self, employee_id: str, data: str):
        return f"Updated record for employee ID {employee_id} with data: {data}"

    def _arun(self, employee_id: str, data: str):
        raise NotImplementedError("This tool does not support async")

class GenerateJobDescriptionTool(BaseTool):
    name = "Generate Job Description"
    description = "Use this to generate a job description for a given title and department."

    def _run(self, job_title: str, department: str):
        return f"Job description for {job_title} in {department}"

    def _arun(self, job_title: str, department: str):
        raise NotImplementedError("This tool does not support async")

class TrackApplicationTool(BaseTool):
    name = "Track Application"
    description = "Use this to update the status of a job application."

    def _run(self, applicant_id: str, status: str):
        return f"Updated application status for applicant {applicant_id} to {status}"

    def _arun(self, applicant_id: str, status: str):
        raise NotImplementedError("This tool does not support async")

class CreateEvaluationTool(BaseTool):
    name = "Create Performance Evaluation"
    description = "Use this to create a performance evaluation for an employee."

    def _run(self, employee_id: str, period: str):
        return f"Created performance evaluation for employee {employee_id} for period {period}"

    def _arun(self, employee_id: str, period: str):
        raise NotImplementedError("This tool does not support async")

def get_all_tools():
    return {
        "internet_search": InternetSearchTool(),
        "query_employee_data": QueryEmployeeDataTool(),
        "update_employee_record": UpdateEmployeeRecordTool(),
        "generate_job_description": GenerateJobDescriptionTool(),
        "track_application": TrackApplicationTool(),
        "create_evaluation": CreateEvaluationTool()
    }
