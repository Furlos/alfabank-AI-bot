#!/bin/bash

echo "Starting Ollama server..."

# Запускаем Ollama в фоне
/bin/ollama serve &

# Ждем пока сервер запустится
echo "Waiting for Ollama to start..."
sleep 15

# Проверяем что сервер работает
if curl -f http://localhost:11434/api/tags; then
    echo "Ollama server is running, pulling model..."

    # Скачиваем модель (можно изменить через переменную окружения)
    ollama pull ${OLLAMA_MODEL:-llama3:8b}

    echo "Model ${OLLAMA_MODEL:-llama3:8b} pulled successfully!"
    echo "Available models:"
    ollama list
else
    echo "Failed to start Ollama server"
    exit 1
fi

# Бесконечно ждем, сохраняя контейнер активным
echo "Ollama is ready to use!"
wait