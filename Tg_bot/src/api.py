import aiohttp
from config import ai_service_endpoint

async def make_request(text: str):
    payload = {"message": text}

    async with aiohttp.ClientSession() as session:
        async with session.post(
                ai_service_endpoint,
                json=payload,
                headers={"accept": "application/json", "Content-Type": "application/json"}
        ) as response:
            if response.status == 200:
                data = await response.json()
                return data.get("content", data)
            else:
                error_text = await response.text()
                return f"Ошибка {response.status}: {error_text}"