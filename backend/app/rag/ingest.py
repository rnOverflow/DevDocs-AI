import os
from dotenv import load_dotenv

load_dotenv()

from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from .embeddings import get_embedding_model

DATA_PATH = "data"
DB_PATH = "db"

def load_documents():
    documents = []

    for root, _, files in os.walk(DATA_PATH):
        for file in files:
            if file.endswith(".py") or file.endswith(".txt") or file.endswith(".md"):
                path = os.path.join(root, file)
                loader = TextLoader(path)
                documents.extend(loader.load())

    return documents

def split_documents(documents):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )
    return splitter.split_documents(documents)

def ingest():
    print("📥 Loading documents...")
    docs = load_documents()

    print("✂️ Splitting documents...")
    chunks = split_documents(docs)

    print("🧠 Creating embeddings...")
    embedding = get_embedding_model()

    print("💾 Storing in Chroma DB...")
    vectordb = Chroma.from_documents(
        documents=chunks,
        embedding=embedding,
        persist_directory=DB_PATH
    )

    print("✅ Ingestion complete!")

if __name__ == "__main__":
     ingest()