from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.rag.pipeline import run_rag, initialize

# ✅ FIRST create app
app = FastAPI()

# ✅ THEN add CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5500",
        "http://127.0.0.1:5500"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ THEN startup event
@app.on_event("startup")
def startup_event():
    initialize()

# ✅ Routes
@app.get("/")
def root():
    return {"message": "RAG API is running 🚀"}

@app.get("/ask")
def ask(query: str):
    return run_rag(query)