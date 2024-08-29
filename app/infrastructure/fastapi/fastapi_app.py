from app.domain.exceptions.app_base_error import (
    AppBaseError,
    AppBaseWarning,
    AppGenericError,
    AppRequestError,
)
from app.infrastructure.fastapi.fastapi_exception_handlers import (
    app_base_error_handler,
    app_base_warning_handler,
    app_generic_error_handler,
    app_request_error_handler,
)
from app.infrastructure.fastapi.routes import router
from fastapi import FastAPI

fastapi_app = FastAPI()

fastapi_app.include_router(router)
fastapi_app.add_exception_handler(AppBaseWarning, app_base_warning_handler)
fastapi_app.add_exception_handler(AppRequestError, app_request_error_handler)
fastapi_app.add_exception_handler(AppGenericError, app_generic_error_handler)
fastapi_app.add_exception_handler(AppBaseError, app_base_error_handler)
