import logging
import requests
from typing import Dict, Any, Optional

logger = logging.getLogger(__name__)


def make_request(message: str) -> str:
    """
    Отправляет запрос к AI модели и возвращает ответ.

    Args:
        message: Текст сообщения для AI

    Returns:
        Ответ от AI модели

    Raises:
        ValueError: При пустом сообщении или ошибках валидации
        requests.exceptions.RequestException: При ошибках сетевого запроса
        KeyError: При неожиданной структуре ответа
        Exception: При других непредвиденных ошибках
    """
    # Валидация входных данных
    if not message or not message.strip():
        raise ValueError("Сообщение не может быть пустым")

    if len(message.strip()) > 1000:
        raise ValueError("Сообщение слишком длинное (максимум 1000 символов)")

    url = "http://model-runner.docker.internal/engines/v1/chat/completions"
    payload = {
        "model": "ai/smollm2:360M-Q4_K_M",
        "messages": [{"role": "user", "content": message.strip()}]
    }

    try:
        logger.info(f"Отправка запроса к AI модели: {message[:50]}...")

        response = requests.post(
            url,
            json=payload,
            timeout=30,  # Таймаут 30 секунд
            headers={"Content-Type": "application/json"}
        )
        response.raise_for_status()  # Выбрасывает исключение для HTTP ошибок

        response_data = response.json()

        # Безопасное извлечение данных из ответа
        if not response_data.get("choices"):
            raise KeyError("В ответе отсутствуют 'choices'")

        first_choice = response_data["choices"][0]
        if not first_choice.get("message") or not first_choice["message"].get("content"):
            raise KeyError("В ответе отсутствует 'message.content'")

        content = first_choice["message"]["content"]

        if not content or not content.strip():
            raise ValueError("Получен пустой ответ от AI модели")

        logger.info("Успешно получен ответ от AI модели")
        return content.strip()

    except requests.exceptions.Timeout:
        logger.error("Таймаут при запросе к AI модели")
        raise requests.exceptions.RequestException("Таймаут при обращении к AI сервису")

    except requests.exceptions.ConnectionError:
        logger.error("Ошибка подключения к AI модели")
        raise requests.exceptions.RequestException("Не удалось подключиться к AI сервису")

    except requests.exceptions.HTTPError as e:
        status_code = e.response.status_code if e.response else "unknown"
        logger.error(f"HTTP ошибка от AI сервиса: {status_code}")
        raise requests.exceptions.RequestException(f"Ошибка AI сервиса: {status_code}")

    except requests.exceptions.RequestException as e:
        logger.error(f"Ошибка запроса к AI модели: {str(e)}")
        raise