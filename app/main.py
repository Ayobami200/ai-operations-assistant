from fastapi import FastAPI
from app.api.ai import router as ai_router

app = FastAPI(title="AI Operations Assistant")

app.include_router(ai_router)


@app.get("/")
def root():
    return {
        "message": "AI Operations Assistant is running"
    }