from app.rag.pipeline import run_rag

query = "What is this document about?"

response = run_rag(query)

print("\n🧠 RESPONSE:\n")
print(response)