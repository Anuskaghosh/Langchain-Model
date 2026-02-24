import pkg_resources

print("LangChain:", pkg_resources.get_distribution("langchain").version)
print("LangChain Core:", pkg_resources.get_distribution("langchain-core").version)
from dotenv import load_dotenv
import langchain

print("dotenv OK")
print("LangChain version:", langchain.__version__)

