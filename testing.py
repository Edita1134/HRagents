from langchain_groq import ChatGroq
import os
llm= ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model_name="llama3-70b-8192",
    temperature=0.5,
    verbose=True
)

print(llm("this is llm call"))