from app.infrastructure.fastapi.fastapi_app import fastapi_app
from uvicorn import run

if __name__ == "__main__":
    run(fastapi_app, host="0.0.0.0", port=8000)
