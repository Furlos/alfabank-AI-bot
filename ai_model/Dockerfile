FROM ollama/ollama:latest

# Устанавливаем curl для healthcheck
RUN apk add --no-cache curl

# Создаем скрипт для запуска
COPY setup.sh /setup.sh
RUN chmod +x /setup.sh

# Запускаем скрипт
CMD ["/setup.sh"]