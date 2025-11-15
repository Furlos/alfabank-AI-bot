async def make_request(message: str) -> str:
    if not message or not message.strip():
        raise ValueError("Сообщение не может быть пустым")

    message = message.strip()
    if len(message) > 1000:
        raise ValueError("Сообщение слишком длинное (максимум 1000 символов)")

    url = "http://localhost:11434/api/generate"  # Используем generate вместо chat - быстрее!
    payload = {
        "model": "tinyllama:1.1b",
        "prompt": message,  # Прямой промпт без системы сообщений
        "stream": False,
        "options": {
            "temperature": 0.1,  # Сильно уменьшаем для скорости и консистентности
            "top_p": 0.5,  # Уменьшаем для скорости
            "top_k": 20,  # Ограничиваем словарь
            "num_predict": 150,  # Уменьшаем длину ответа
            "num_thread": 4,  # Указываем количество потоков
            "num_gpu": 1,  # Используем GPU если доступен
            "main_gpu": 0,  # Основная GPU
            "low_vram": False,  # Отключаем если достаточно памяти
            "mirostat": 0,  # Отключаем для скорости
            "repeat_penalty": 1.0,  # Минимальный penalty
            "seed": 42  # Фиксируем seed для консистентности
        },
        "system": "Ты - строгий бизнес-ассистент. Отвечай ТОЛЬКО на профессиональные вопросы: бизнес, юриспруденция, договоры, налоги. На остальные вопросы отвечай: 'Извините, но это выходит за рамки моей компетенции как бизнес-ассистента.' Отвечай кратко и по делу."
    }

    timeout = aiohttp.ClientTimeout(total=30)  # Уменьшаем таймаут

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