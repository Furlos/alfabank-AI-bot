"""API smoke tests requiring no external Ollama server."""
import pytest
from fastapi.testclient import TestClient

import api
from main import app

client = TestClient(app)


def test_health():
    result = client.get("/health")
    assert result.status_code == 200
    assert result.json()["model_ready"] == "not_checked"


def test_empty_messages_are_rejected():
    result = client.post("/ai/make_request", json={"message": ""})
    assert result.status_code == 422


def test_too_long_messages_are_rejected():
    result = client.post("/ai/make_request", json={"message": "x" * 1001})
    assert result.status_code == 422


def test_proxy_success_without_real_model(monkeypatch):
    async def fake_model(message: str):
        return "Пример ответа: " + message

    monkeypatch.setattr(api, "make_request", fake_model)
    result = client.post("/ai/make_request", json={"message": "Привет"})
    assert result.status_code == 200
    assert result.json() == {"content": "Пример ответа: Привет", "success": True}


def test_proxy_unavailable(monkeypatch):
    import aiohttp

    async def fake_model(message: str):
        raise aiohttp.ClientConnectionError("Fake connection failure")

    monkeypatch.setattr(api, "make_request", fake_model)
    result = client.post("/ai/make_request", json={"message": "Привет"})
    assert result.status_code == 503
    assert result.json()["detail"] == "Model service temporarily unavailable."
