import uvicorn
from fastapi import FastAPI

from api import ai_router

app = FastAPI()
app.include_router(ai_router)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=3000)