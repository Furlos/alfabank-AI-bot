"""LLM proxy API with validation and safe logging."""
import logging

import aiohttp
from fastapi import APIRouter, Body, HTTPException
from pydantic import BaseModel, Field

from handlers import make_request

logger = logging.getLogger(__name__)
ai_router = APIRouter(prefix="/ai", tags=["ai"])


class AIRequest(BaseModel):
    message: str = Field(..., min_length=1, max_length=1000)


class AIResponse(BaseModel):
    content: str
    success: bool = True


@ai_router.post("/make_request", response_model=AIResponse)
async def make_ai_request(ai_request: AIRequest = Body(...)):
    # Avoid logging users' confidential questions in plaintext.
    logger.info("New LLM request (characters=%s)", len(ai_request.message))
    try:
        result = await make_request(ai_request.message)
        return AIResponse(content=result)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    except (aiohttp.ClientError, TimeoutError) as exc:
        logger.warning("Ollama unavailable (%s)", type(exc).__name__)
        raise HTTPException(status_code=503, detail="Model service temporarily unavailable.") from exc
    except Exception as exc:
        logger.exception("Unexpected model proxy failure")
        raise HTTPException(status_code=500, detail="Internal AI service error.") from exc
