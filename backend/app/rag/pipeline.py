from .retriever import get_retriever
from .generator import get_llm

def run_rag(query: str):
    retriever = get_retriever()
    llm = get_llm()

    docs = retriever.invoke(query)

    context = "\n".join([doc.page_content for doc in docs])

    prompt = f"""
You are an AI assistant. Answer the question using the context below.

Context:
{context}

Question:
{query}

Answer:
"""

    response = llm(prompt)
    generated_text = response[0]["generated_text"]

# Extract only answer part
    if "Answer:" in generated_text:
        return generated_text.split("Answer:")[-1].strip()

    return generated_text.strip()