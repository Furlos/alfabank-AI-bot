"""Environment-based Ollama connection settings."""
import os

ollama_url = os.getenv("OLLAMA_BASE_URL", "http://ai_model:11434").rstrip("/") + "/api/generate"
ollama_model = os.getenv("OLLAMA_MODEL", "llama3:8b")
