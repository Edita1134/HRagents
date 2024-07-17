from crewai import Crew, Process
from hr_agents import (
    recruitment_specialist,
    interviewer,
    onboarding_specialist,
    employee_relations_manager,
    training_developer
)
from tasks import (
    recruitment_task,
    interview_task,
    onboarding_task,
    employee_relations_task,
    training_development_task
)
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def create_hr_crew(process_type=Process.sequential):
    """
    Create and return an HR-focused crew.
    
    Args:
    process_type (Process): The type of process to use (default: sequential)
    
    Returns:
    Crew: A configured HR crew
    """
    hr_crew = Crew(
        agents=[
            recruitment_specialist,
            interviewer,
            onboarding_specialist,
            employee_relations_manager,
            training_developer
        ],
        tasks=[
            recruitment_task,
            interview_task,
            onboarding_task,
            employee_relations_task,
            training_development_task
        ],
        process=process_type,
        verbose=True  # For enhanced feedback
    )
    return hr_crew

def run_hr_process(job_position, department, skill_area, issue=None):
    try:
        hr_crew = create_hr_crew()
        
        inputs = {
            'job_position': job_position,
            'department': department,
            'skill_area': skill_area,
            'issue': issue
        }
        
        logging.info(f"Starting HR process for {job_position} in {department}")
        result = hr_crew.kickoff(inputs=inputs)
        logging.info("HR process completed successfully")
        return result
    except Exception as e:
        logging.error(f"An error occurred during the HR process: {str(e)}")
        raise

# Example usage
if __name__ == "__main__":
    job_position = "Software Engineer"
    department = "Engineering"
    skill_area = "Python Programming"
    issue = "Work-from-home policy disagreements"
    
    result = run_hr_process(job_position, department, skill_area, issue)
    print(result)
