FROM python:3.12-alpine AS builder
WORKDIR /app

RUN apk add --no-cache \
    gcc \
    musl-dev \
    libffi-dev

RUN pip install --no-cache-dir uv

COPY pyproject.toml ./

RUN uv pip install --system --no-cache -r pyproject.toml

FROM python:3.12-alpine
WORKDIR /app

RUN adduser -D backend && \
    chown backend:backend /app

COPY --from=builder /usr/local/lib/python3.12/site-packages/ /usr/local/lib/python3.12/site-packages/
COPY --from=builder /usr/local/bin/ /usr/local/bin/

COPY src/ .

ENV PYTHONUNBUFFERED=1 \
    PYTHONPATH=/app

USER backend
EXPOSE 3000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "3000"]