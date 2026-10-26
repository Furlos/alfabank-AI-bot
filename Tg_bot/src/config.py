"""Bot configuration."""
import os
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("BOT_TOKEN")
ai_service_endpoint = os.getenv("AI_SERVICE_ENDPOINT", "http://ai_service:3000/ai/make_request")
