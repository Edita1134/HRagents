from crewai import Agent
from dotenv import load_dotenv
from tools import get_all_tools
load_dotenv()
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
import os

# Initialize the Groq LLM
llm = ChatOpenAI(
    api_key="hjbb",
    model_name="mistralai/Mistral-7B-Instruct-v0.3",
    temperature=0.5,
    verbose=True,
    base_url=os.getenv("LLM_URL")
)

# Get all tools
tools = list(get_all_tools().values())  # Convert dictionary to list

recruitment_specialist = Agent(
    role='Recruitment Specialist',
    goal='Source and evaluate candidates for open positions',
    backstory="As an experienced recruiter with a keen eye for talent, you excel at identifying the best candidates for various roles across industries.",
    verbose=True,
    allow_delegation=True,
    tools=tools,
    llm=llm
)

interviewer = Agent(
    role='Interview Conductor',
    goal='Conduct thorough interviews and assess candidate fit',
    backstory="With years of experience in behavioral interviewing and candidate assessment, you're skilled at evaluating both technical skills and cultural fit.",
    verbose=True,
    allow_delegation=True,
    tools=tools,
    llm=llm
)

onboarding_specialist = Agent(
    role='Onboarding Coordinator',
    goal='Create comprehensive onboarding plans for new hires',
    backstory="You're passionate about creating smooth transitions for new employees, ensuring they have all the resources and information needed to succeed.",
    verbose=True,
    allow_delegation=True,
    tools=tools,
    llm=llm
)

employee_relations_manager = Agent(
    role='Employee Relations Manager',
    goal='Address and resolve employee concerns and conflicts',
    backstory="With a background in conflict resolution and a deep understanding of workplace dynamics, you excel at maintaining a positive work environment.",
    verbose=True,
    allow_delegation=True,
    tools=tools,
    llm=llm
)

training_developer = Agent(
    role='Training and Development Specialist',
    goal='Design and implement effective training programs',
    backstory="As an expert in adult learning and professional development, you create engaging and effective training programs that enhance employee skills.",
    verbose=True,
    allow_delegation=True,
    tools=tools,
    llm=llm
)
