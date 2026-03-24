from langchain_community.vectorstores import Chroma
from .embeddings import get_embedding_model

def get_retriever():
    embedding = get_embedding_model()

    vectordb = Chroma(
        persist_directory="db",
        embedding_function=embedding
    )

    return vectordb.as_retriever()