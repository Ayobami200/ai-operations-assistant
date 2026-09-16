from fastapi import APIRouter
from app.schemas.ai import ChatRequest, ChatResponse

router = APIRouter(prefix="/ai", tags=["AI"])


@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    return {
        "response": f"You said: {request.message}"
    }