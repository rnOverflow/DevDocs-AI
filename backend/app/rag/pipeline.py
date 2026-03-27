from urllib import response
from .retriever import get_retriever
from .generator import get_llm

retriever = None
llm = None

def initialize():
    global retriever, llm
    retriever = get_retriever()
    llm = get_llm()

chat_history = []

def run_rag(query: str):
    global retriever, llm, chat_history

    docs = retriever.invoke(query)
    context = "\n".join([doc.page_content for doc in docs])

    history_text = "\n".join(chat_history[-4:])  # last 4 messages

    prompt = f"""
You are an AI assistant.

Conversation so far:
{history_text}

Context:
{context}

User Question:
{query}

Answer:
"""

    response = llm.invoke(prompt)
    answer = response.content.strip()

    # save history
    chat_history.append(f"User: {query}")
    chat_history.append(f"AI: {answer}")

    sources = list(set([doc.metadata.get("source", "Unknown") for doc in docs]))

    return {
        "answer": answer,
        "sources": sources
    }