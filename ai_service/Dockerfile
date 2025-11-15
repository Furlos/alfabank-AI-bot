FROM python:3.12-alpine AS builder
WORKDIR /app

# Устанавливаем системные зависимости
RUN apk add --no-cache \
    gcc \
    musl-dev \
    libffi-dev

# Устанавливаем uv
RUN pip install --no-cache-dir uv

# Копируем файлы зависимостей
COPY pyproject.toml ./

# Устанавливаем зависимости через uv
RUN uv pip install --system --no-cache -r pyproject.toml

FROM python:3.12-alpine
WORKDIR /app

# Создаем пользователя
RUN adduser -D backend && \
    chown backend:backend /app

# Копируем установленные зависимости из builder stage
COPY --from=builder /usr/local/lib/python3.12/site-packages/ /usr/local/lib/python3.12/site-packages/
COPY --from=builder /usr/local/bin/ /usr/local/bin/

# Копируем исходный код
COPY src/ ./src/

# Настраиваем переменные окружения
ENV PYTHONUNBUFFERED=1 \
    PYTHONPATH=/app

USER backend
EXPOSE 3000

CMD ["uvicorn", "src/main:app", "--host", "0.0.0.0", "--port", "3000"]