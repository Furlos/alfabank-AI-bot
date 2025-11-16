#!/bin/bash

echo "Starting Ollama server..."

# Запускаем Ollama в фоне
/bin/ollama serve &

# Ждем пока сервер запустится
echo "Waiting for Ollama to start..."
sleep 20

# Проверяем что сервер работает (пробуем несколько раз)
for i in {1..10}; do
    if curl -f http://localhost:11434/api/tags > /dev/null 2>&1; then
        echo "Ollama server is running, pulling model..."

        # Скачиваем модель
        ollama pull ${OLLAMA_MODEL:-llama3:8b}

        echo "Model ${OLLAMA_MODEL:-llama3:8b} pulled successfully!"
        echo "Available models:"
        ollama list

        # Бесконечно ждем
        echo "Ollama is ready to use!"
        wait
        exit 0
    else
        echo "Waiting for Ollama to start... (attempt $i/10)"
        sleep 5
    fi
done

echo "Failed to start Ollama server after 10 attempts"
exit 1