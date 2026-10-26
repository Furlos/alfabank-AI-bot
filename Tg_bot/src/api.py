"""Internal HTTP client for the AI service."""
import asyncio
import aiohttp

from config import ai_service_endpoint


async def make_request(text: str) -> str:
    if not isinstance(text, str) or not text.strip():
        return "Отправьте текстовый вопрос."
    try:
        timeout = aiohttp.ClientTimeout(total=190)
        async with aiohttp.ClientSession(timeout=timeout) as session:
            async with session.post(
                ai_service_endpoint,
                json={"message": text[:1000]},
            ) as response:
                if response.status != 200:
                    return "Сервис временно недоступен. Попробуйте позже."
                data = await response.json()
                return str(data.get("content") or "Пустой ответ модели.")
    except (aiohttp.ClientError, asyncio.TimeoutError):
        return "Сервис временно недоступен. Попробуйте позже."
