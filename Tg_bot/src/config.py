import os
from dotenv import load_dotenv

# Загружаем переменные из .env файла
load_dotenv()

token = os.getenv("BOT_TOKEN")
ai_service_endpoint = "http://localhost:3000/ai/make_request"