from crewai import Task
from tools import get_all_tools
from hr_agents import recruitment_specialist, interviewer, onboarding_specialist, employee_relations_manager, training_developer

tools = list(get_all_tools().values())  # Convert dictionary to list

recruitment_task = Task(
    description=(
        "Source and evaluate candidates for the {job_position} role. "
        "Focus on identifying the top 5 candidates based on their qualifications, "
        "experience, and potential cultural fit. "
        "Your final report should include a summary of each candidate's strengths "
        "and any potential areas of concern."
    ),
    agent=recruitment_specialist,
    expected_output="A report summarizing the top 5 candidates' strengths and areas of concern."
)

interview_task = Task(
    description=(
        "Conduct in-depth interviews with the candidates for the {job_position} role. "
        "Assess their technical skills, problem-solving abilities, and cultural fit. "
        "Provide a detailed evaluation of each candidate, including their strengths, "
        "weaknesses, and overall suitability for the role."
    ),
    agent=interviewer,
    expected_output="A detailed evaluation of each candidate's strengths, weaknesses, and overall suitability for the role."
)

onboarding_task = Task(
    description=(
        "Create a comprehensive onboarding plan for new hires in the {department}. "
        "Include necessary paperwork, orientation sessions, introductions to key team members, "
        "and a schedule for the first week. Ensure the plan covers company policies, "
        "department-specific information, and any required training."
    ),
    agent=onboarding_specialist,
    expected_output="A comprehensive onboarding plan including paperwork, orientation sessions, introductions, and a first-week schedule."
)

employee_relations_task = Task(
    description=(
        "Address and propose solutions for the ongoing conflict in the {department} "
        "regarding {issue}. Analyze the situation, identify the root causes, "
        "and suggest appropriate interventions or mediation strategies. "
        "Consider the impact on team dynamics and overall productivity."
    ),
    agent=employee_relations_manager,
    expected_output="A report with proposed solutions for the conflict, including root cause analysis and intervention strategies."
)

training_development_task = Task(
    description=(
        "Design a comprehensive training program for {skill_area} tailored to the needs "
        "of the {department}. Include learning objectives, course outline, "
        "delivery methods, and assessment criteria. Consider both in-person "
        "and online learning components."
    ),
    agent=training_developer,
    expected_output="A comprehensive training program with learning objectives, course outline, delivery methods, and assessment criteria."
)

