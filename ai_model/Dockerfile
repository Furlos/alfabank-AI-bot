FROM ollama/ollama:latest

# Копируем скрипт для запуска
COPY setup.sh /setup.sh
RUN chmod +x /setup.sh

# Запускаем скрипт
CMD ["/setup.sh"]