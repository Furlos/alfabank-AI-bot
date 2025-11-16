FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    curl ca-certificates && \
    rm -rf /var/lib/apt/lists/*

# Установка Ollama
RUN curl -fsSL https://ollama.com/install.sh | sh

# MODEL задаётся в docker-compose — здесь НЕ задаём!
# ENV OLLAMA_MODEL=...

CMD sh -c "ollama serve & sleep 5 && ollama pull $OLLAMA_MODEL && wait"
