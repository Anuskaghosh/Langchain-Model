from transformers import pipeline
from langchain_huggingface import HuggingFacePipeline, ChatHuggingFace

# Explicit HF pipeline (NO duplicate device)
hf_pipeline = pipeline(
    task="text-generation",
    model="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    temperature=0.5,
    max_new_tokens=100,
    torch_dtype="float32",
)

llm = HuggingFacePipeline(pipeline=hf_pipeline)

model = ChatHuggingFace(llm=llm)

result = model.invoke("What is the capital of India?")
print(result.content)


model = ChatHuggingFace(llm=llm)

result = model.invoke("What is the capital of India?")
print(result.content)


model = ChatHuggingFace(llm=llm)

result = model.invoke("what is the capital of India?")
print(result.content)
