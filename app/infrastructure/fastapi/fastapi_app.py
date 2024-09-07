from fastapi import FastAPI

from app.infrastructure.fastapi.routes import router

fastapi_app = FastAPI()

fastapi_app.include_router(router)
