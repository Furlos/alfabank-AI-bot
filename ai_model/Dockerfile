FROM ollama/ollama:latest

# Запускаем Ollama и загружаем модель при старте
CMD sh -c "/bin/ollama serve & sleep 20 && ollama pull ${OLLAMA_MODEL:-llama3:8b} && wait"