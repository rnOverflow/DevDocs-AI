from fastapi import APIRouter
from pydantic import BaseModel
from app.rag.pipeline import run_rag

router = APIRouter()

class QueryRequest(BaseModel):
    query: str

@router.post("/ask")
def ask_question(request: QueryRequest):
    answer = run_rag(request.query)
    return {"answer": answer}