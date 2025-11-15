FROM python:3.12-alpine AS builder
WORKDIR /app
RUN apk add --no-cache \
    gcc \
    musl-dev \
    libffi-dev
RUN pip install --no-cache-dir uv
COPY pyproject.toml ./
RUN uv pip compile -o requirements.txt pyproject.toml
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt
FROM python:3.12-alpine
WORKDIR /app
RUN adduser -D backend && \
    chown backend:backend /app
COPY --from=builder --chown=backend:backend / /usr/local
COPY src/ ./src/
ENV PYTHONUNBUFFERED=1 \
    PYTHONPATH=/app
USER backend
EXPOSE 3000
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "3000"]