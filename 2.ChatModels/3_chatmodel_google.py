import os
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")
print(api_key)
if not api_key:
	raise ValueError("GOOGLE_API_KEY environment variable is not set")

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", google_api_key=api_key)

try:
	result = model.invoke('what is the capital of India')
	print(result.content)
except Exception as e:
	print(f"Error: {e}")