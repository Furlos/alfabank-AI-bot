# Alfabank AI Bot — Telegram + FastAPI + Ollama prototype

Educational team prototype of a business-oriented AI assistant. This repository is **not** affiliated with or endorsed by Alfa-Bank.

**Status:** source code and a repeatable local Docker setup are provided. The Telegram bot and the model are **not independently verified to be available online now**. Do not treat an old green badge, public bot handle or presentation as evidence of current uptime.

## Architecture

```text
Telegram user -> Aiogram bot -> FastAPI AI proxy -> Ollama -> selected local model
```

- `Tg_bot/`: Telegram user interface.
- `ai_service/`: model API proxy and response handling.
- `ai_model/`: legacy container build (Compose now uses the official Ollama image).
- `docker-compose.yml`: local infrastructure.

## Local run

Requires Docker Compose, enough RAM/disk space for the selected model and a Telegram bot token.

1. Copy `.env.example` to `.env` and insert your real `BOT_TOKEN`.
2. Run `docker compose up -d --build`.
3. Pull the model (one-time download, can take several GB):

```bash
docker compose exec ai_model ollama pull llama3:8b
```

If you set a different `OLLAMA_MODEL` in `.env`, pull that exact model instead. The local system needs enough memory to load it.

4. Try the health endpoint on the Docker host:

```text
http://127.0.0.1:3000/health
```

5. Send a message to your Telegram bot. View logs with `docker compose logs -f tg-bot ai_service ai_model`.

`GET /health` checks that FastAPI is up; it does **not** imply the model has finished downloading or is ready.

The Ollama API is not exposed publicly; the FastAPI demo is bound only to `127.0.0.1` on the host. Never commit your bot token.

## Tests

```bash
cd ai_service
pip install -r requirements.txt pytest httpx
PYTHONPATH=src pytest -q
```

CI tests validation and error behavior using mocked model calls; **no real Ollama inference is tested**.

## Safety and limitations

- Generated answers can be wrong. The bot is a technical demo, **not** a replacement for qualified legal or financial advisers.
- Model inference requires separately available CPU/GPU resources and is not a free always-on cloud service.
- The demo does not include user authentication, billing, robust rate limits, uptime guarantees or production monitoring.
- Telegram UI flow and real model responses still need end-to-end verification on the target machine.

## Team contributions

The original prototype was built as a team exercise: Lev Primak (architecture/integration/deployment), Larionov Nikita (Telegram UI), Smirnova Mariya (business analysis), and Reval Sadrislamov (QA/design). Attribution is retained from the original project documentation.

## Portfolio

This project demonstrates asynchronous Telegram integration, FastAPI, HTTP requests, Docker Compose, validation and LLM proxying.

For service inquiries, see the developer profile: [Furlos](https://github.com/Furlos).
