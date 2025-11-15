import aiohttp
async def make_request(text: str):
    url = "http://localhost:3000/ai/make_request"  # Измените на localhost

    payload = {"message": text}

    async with aiohttp.ClientSession() as session:
        async with session.post(
                url,
                json=payload,
                headers={"accept": "application/json", "Content-Type": "application/json"}
        ) as response:
            if response.status == 200:
                data = await response.json()
                return data.get("content", data)
            else:
                error_text = await response.text()
                return f"Ошибка {response.status}: {error_text}"