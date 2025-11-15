import aiohttp


async def make_request(message: str) -> str:
    if not message or not message.strip():
        raise ValueError("Сообщение не может быть пустым")

    message = message.strip()
    if len(message) > 1000:
        raise ValueError("Сообщение слишком длинное (максимум 1000 символов)")

    url = "http://localhost:11434/api/generate"
    payload = {
        "model": "tinyllama:1.1b",  # Хороший выбор для CPU
        "prompt": message,
        "stream": False,
        "options": {
            "temperature": 0.1,
            "top_p": 0.5,
            "top_k": 20,
            "num_predict": 512,  # Ограничиваем длину ответа
            "mirostat": 0,
            "repeat_penalty": 1.0,
            "seed": 42,
            # Параметры для оптимизации CPU
            "num_thread": 8,  # Используем больше потоков процессора
            "num_batch": 512,  # Размер батча для обработки
            "use_mlock": True,  # Блокировка памяти для стабильности
            "use_mmap": True,  # Использование mmap для эффективности
        },
        "system": "Ты - строгий бизнес-ассистент. Отвечай ТОЛЬКО на профессиональные вопросы: бизнес, юриспруденция, договоры, налоги. На остальные вопросы отвечай: 'Извините, но это выходит за рамки моей компетенции как бизнес-ассистента.' Отвечай кратко и по делу."
    }

    timeout = aiohttp.ClientTimeout(total=45)  # Немного увеличим для CPU

    async with aiohttp.ClientSession(timeout=timeout) as session:
        try:
            async with session.post(
                    url,
                    json=payload,
                    headers={"Content-Type": "application/json"}
            ) as response:
                response.raise_for_status()
                response_data = await response.json()

                content = response_data["response"]

                if not content or not content.strip():
                    raise ValueError("Получен пустой ответ от AI модели")

                return content.strip()

        except aiohttp.ClientError as e:
            raise aiohttp.ClientError(f"Ошибка при обращении к Ollama: {str(e)}")