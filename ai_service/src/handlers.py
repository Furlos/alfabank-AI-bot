import aiohttp
from typing import Optional


async def make_request(message: str) -> str:
    """
    Асинхронно отправляет запрос к AI модели и возвращает ответ.

    Args:
        message: Текст сообщения для AI (1-1000 символов)

    Returns:
        Ответ от AI модели

    Raises:
        ValueError: При пустом сообщении или ошибках валидации
        aiohttp.ClientError: При ошибках сетевого запроса
        KeyError: При неожиданной структуре ответа
    """
    if not message or not message.strip():
        raise ValueError("Сообщение не может быть пустым")

    message = message.strip()
    if len(message) > 1000:
        raise ValueError("Сообщение слишком длинное (максимум 1000 символов)")

    url = "http://model-runner.docker.internal/engines/v1/chat/completions"
    payload = {
        "model": "ai/smollm2:360M-Q4_K_M",
        "messages": [{"role": "user", "content": message}]
    }

    timeout = aiohttp.ClientTimeout(total=30)

    async with aiohttp.ClientSession(timeout=timeout) as session:
        try:
            async with session.post(
                    url,
                    json=payload,
                    headers={"Content-Type": "application/json"}
            ) as response:
                response.raise_for_status()
                response_data = await response.json()

                # Извлечение ответа из структуры
                content = response_data["choices"][0]["message"]["content"]

                if not content or not content.strip():
                    raise ValueError("Получен пустой ответ от AI модели")

                return content.strip()

        except aiohttp.ClientError as e:
            raise aiohttp.ClientError(f"Ошибка при обращении к AI сервису: {str(e)}")