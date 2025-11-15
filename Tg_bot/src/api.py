import aiohttp

async def make_request(text: str):
    url = "http://ai_service:3000/ai/make_request"
    params = {"message": text}

    async with aiohttp.ClientSession() as session:
        async with session.post(url, params=params, headers={"accept": "application/json"}) as response:
            if response.status == 200:
                data = await response.json()
                return data
            else:
                error_text = await response.text()
                return f"Ошибка {response.status}: {error_text}"