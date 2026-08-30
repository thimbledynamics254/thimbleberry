import os
import secrets
from typing import Optional
from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Thimbleberry API", version="1.0.0",
              docs_url="/v1/docs", openapi_url="/v1/openapi.json")

THIMBLEBERRY_API_KEY = os.getenv("THIMBLEBERRY_API_KEY", "")

def authenticate(authorization: Optional[str]):
    if not THIMBLEBERRY_API_KEY:
        raise HTTPException(500, "API authentication is not configured")
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(401, "Missing Bearer token")
    supplied = authorization[7:].strip()
    if not secrets.compare_digest(supplied, THIMBLEBERRY_API_KEY):
        raise HTTPException(401, "Invalid API key")

class ChatRequest(BaseModel):
    message: str
    conversation_id: Optional[str] = None
    model: Optional[str] = "thimble-ai"

@app.get("/v1/health")
def health():
    return {"success": True, "service": "thimbleberry-api",
            "version": "1.0.0", "status": "online"}

@app.post("/v1/ai/chat")
def ai_chat(payload: ChatRequest, authorization: Optional[str] = Header(None)):
    authenticate(authorization)
    raise HTTPException(501, "AI provider is not configured yet")

@app.get("/v1/ai/models")
def ai_models(authorization: Optional[str] = Header(None)):
    authenticate(authorization)
    return {"success": True, "models": [{"id": "thimble-ai",
            "name": "Thimble AI", "status": "available"}]}

@app.get("/v1/users/me")
def current_user(authorization: Optional[str] = Header(None)):
    authenticate(authorization)
    return {"success": True, "message": "Authentication successful"}
