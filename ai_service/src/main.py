"""AI service ASGI app."""
import uvicorn
from fastapi import FastAPI
from api import ai_router

app = FastAPI(title="Business assistant demo", version="0.2.0")
app.include_router(ai_router)


@app.get("/health")
async def health():
    # Checks only that FastAPI is running, not whether the LLM is loaded.
    return {"status": "ok", "model_ready": "not_checked"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=3000)
