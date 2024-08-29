from app.domain.exceptions.app_base_error import (
    AppBaseError,
    AppBaseWarning,
    AppGenericError,
    AppRequestError,
)
from fastapi import Request
from fastapi.responses import JSONResponse
from starlette import status


async def app_base_warning_handler(request: Request, exc: AppBaseWarning):
    return JSONResponse(
        status_code=status.HTTP_202_ACCEPTED,
        content={"detail": exc.dict()},
    )


async def app_request_error_handler(request: Request, exc: AppRequestError):
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={"detail": exc.dict()},
    )


async def app_generic_error_handler(request: Request, exc: AppGenericError):
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={"detail": exc.dict()},
    )


async def app_base_error_handler(request: Request, exc: AppBaseError):
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={"detail": exc.dict()},
    )
