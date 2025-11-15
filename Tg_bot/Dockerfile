FROM python:3.13-alpine AS builder
WORKDIR /frontend
RUN pip install --no-cache-dir uv
COPY pyproject.toml uv.lock ./
RUN uv pip compile -o requirements.txt pyproject.toml

FROM python:3.13-alpine
WORKDIR /frontend
RUN adduser -D frontend && chown frontend:frontend /frontend
COPY --from=builder /frontend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY --chown=frontend:frontend src ./
USER frontend
CMD ["python", "src/main.py"]