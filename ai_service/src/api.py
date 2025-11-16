from typing import Optional
import aiohttp
import logging

from fastapi import APIRouter, HTTPException, status, Body
from pydantic import BaseModel, Field

from handlers import make_request

# Настройка логирования
logger = logging.getLogger(__name__)


# Модели Pydantic для валидации
class AIRequest(BaseModel):
    message: str = Field(..., min_length=1, max_length=1000, description="Сообщение для AI")


class AIResponse(BaseModel):
    content: str
    success: bool = True


class ErrorResponse(BaseModel):
    error: str
    details: Optional[str] = None


# Роутер
ai_router = APIRouter(prefix="/ai", tags=["ai"])


@ai_router.post(
    "/make_request",
    response_model=AIResponse,
    responses={
        400: {"model": ErrorResponse, "description": "Неверный запрос"},
        500: {"model": ErrorResponse, "description": "Внутренняя ошибка сервера"},
        503: {"model": ErrorResponse, "description": "Сервис AI недоступен"},
    },
    summary="Отправить запрос к AI",
    description="Отправляет сообщение к AI модели и возвращает ответ"
)
async def make_ai_request(ai_request: AIRequest = Body(...)):
    """
    Обрабатывает запросы к AI модели.

    Параметры:
    - **message**: Текст сообщения для AI (1-1000 символов)

    Возвращает:
    - Ответ от AI модели с флагом успеха
    """
    try:
        logger.info(f"Получен запрос к AI: {ai_request.message[:50]}...")

        content = await make_request(ai_request.message)

        logger.info("Успешно получен ответ от AI модели")
        return AIResponse(content=content, success=True)

    except ValueError as e:
        logger.warning(f"Ошибка валидации запроса: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={"error": "Неверный запрос", "details": str(e)}
        )

    except aiohttp.ClientError as e:
        logger.error(f"Ошибка подключения к AI сервису: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail={"error": "Сервис AI временно недоступен", "details": str(e)}
        )

    except Exception as e:
        logger.error(f"Непредвиденная ошибка при обработке запроса: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail={"error": "Внутренняя ошибка сервера", "details": "Попробуйте позже"}
        )