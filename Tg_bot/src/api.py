import aiohttp
import json


async def make_request(text: str):
    url = "http://ai_service:3000/ai/make_request"

    # Создаем JSON тело запроса вместо параметров URL
    payload = {"message": text}

    async with aiohttp.ClientSession() as session:
        async with session.post(
                url,
                json=payload,  # Используем json вместо params для передачи тела запроса
                headers={"accept": "application/json", "Content-Type": "application/json"}
        ) as response:
            if response.status == 200:
                data = await response.json()
                # Предполагаем, что ответ имеет структуру AIResponse
                return data.get("content", data)
            else:
                error_text = await response.text()
                return f"Ошибка {response.status}: {error_text}"