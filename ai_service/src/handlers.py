import aiohttp
from typing import Optional


async def make_request(message: str) -> str:
    """
    Асинхронно отправляет запрос к AI модели через Ollama и возвращает ответ.

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

    # Подключаемся к Ollama на хост-машине
    url = "http://localhost:11434/api/chat"
    payload = {
        "model": "llama3:8b",  # Используем установленную модель
        "messages": [
            {
                "role": "user",
                "content": "Ты - строгий бизнес-ассистент для бизнес-менеджера. Отвечай ТОЛЬКО на профессиональные вопросы связанные с: бизнесом, юридическими аспектами, корпоративным правом, договорами, налогами, коммерческой деятельностью, управлением компанией. На все остальные вопросы (личные, развлекательные, технические, не связанные с бизнесом) отвечай строго: 'Извините, но это выходит за рамки моей компетенции как бизнес-ассистента. Я могу помочь только с вопросами бизнеса и юриспруденции.' Сохраняй официальный деловой стиль. Отвечай кратко и по делу."
            }
        ],
        "stream": False,
        "options": {
            "temperature": 0.5,
            "top_p": 0.9,  # Еще более строгий отбор
            "max_tokens": 300
        }
    }

    timeout = aiohttp.ClientTimeout(total=90)  # Увеличиваем таймаут для больших моделей

    async with aiohttp.ClientSession(timeout=timeout) as session:
        try:
            async with session.post(
                url,
                json=payload,
                headers={"Content-Type": "application/json"}
            ) as response:
                response.raise_for_status()
                response_data = await response.json()

                # Извлечение ответа из структуры Ollama
                content = response_data["message"]["content"]

                if not content or not content.strip():
                    raise ValueError("Получен пустой ответ от AI модели")

                return content.strip()

        except aiohttp.ClientError as e:
            raise aiohttp.ClientError(f"Ошибка при обращении к Ollama: {str(e)}")
