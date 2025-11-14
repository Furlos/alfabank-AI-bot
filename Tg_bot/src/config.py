import os
from dotenv import load_dotenv

# Загружаем переменные из .env файла
load_dotenv()

token = os.getenv("BOT_TOKEN")
url = os.getenv("API_URL")

# Проверка обязательных переменных
if not token:
    raise ValueError("BOT_TOKEN не установлен в переменных окружения")