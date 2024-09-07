from app.infrastructure.fastapi.routes import router
from fastapi import FastAPI

fastapi_app = FastAPI()

fastapi_app.include_router(router)
