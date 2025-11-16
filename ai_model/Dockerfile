FROM ollama/ollama:latest

ENV OLLAMA_MODEL=llama3:8b

CMD ["ollama serve & sleep 5 && ollama pull $OLLAMA_MODEL && wait"]
