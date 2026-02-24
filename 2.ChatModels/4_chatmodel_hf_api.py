from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

model_id = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"

tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    dtype=torch.float32
)

prompt = "<|system|>You are a helpful assistant.<|user|>What is the capital of pakistan?<|assistant|>"

inputs = tokenizer(prompt, return_tensors="pt")

outputs = model.generate(
    **inputs,
    max_new_tokens=30,
    do_sample=False,
    pad_token_id=tokenizer.eos_token_id,
    eos_token_id=tokenizer.convert_tokens_to_ids("<|user|>")
)

text = tokenizer.decode(outputs[0], skip_special_tokens=True)
answer = text.split("<|assistant|>")[-1].split("<|user|>")[0].strip()
print(answer)




