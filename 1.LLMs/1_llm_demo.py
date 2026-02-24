from langchain_openai import OpenAI
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Create LLM object
llm = OpenAI(model="gpt-3.5-turbo-instruct")

# Make request
result = llm.invoke("What is the capital of India?")

print(result)
