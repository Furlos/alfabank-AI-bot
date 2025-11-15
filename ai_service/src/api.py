from fastapi import APIRouter, HTTPException, Body

from handlers import make_request

ai_router = APIRouter(prefix="/ai", tags=["ai"])

@ai_router.post("/make_request")
async def make_ai_request(message: str):
    try:
        return make_request(message)
    except:
        raise HTTPException(500)