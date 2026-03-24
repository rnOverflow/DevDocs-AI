from transformers import pipeline

def get_llm():
    return pipeline(
        "text-generation",
        model="distilgpt2",
        max_new_tokens=150,   # ✅ only controls output length
        do_sample=True
    )