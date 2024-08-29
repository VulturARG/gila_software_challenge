from functools import wraps
from fastapi import Request, HTTPException
from starlette import status

from app.domain.exceptions.app_base_error import AppGenericError, AppBaseError, AppBaseWarning, AppRequestError


def handle_exceptions(
    generic_error_status=status.HTTP_500_INTERNAL_SERVER_ERROR,
    global_status=status.HTTP_400_BAD_REQUEST,
    warning_status=status.HTTP_202_ACCEPTED,
    request_error_status=status.HTTP_404_NOT_FOUND,
):
    def decorator(func):
        @wraps(func)
        async def wrapper(request: Request, *args, **kwargs):
            try:
                return await func(request, *args, **kwargs)
            except AppBaseWarning as error:
                raise HTTPException(
                    status_code=warning_status,
                    detail=error.dict()
                )
            except AppRequestError as error:
                raise HTTPException(
                    status_code=request_error_status,
                    detail=error.dict()
                )
            except AppGenericError as error:
                raise HTTPException(
                    status_code=generic_error_status,
                    detail=error.dict()
                )
            except AppBaseError as error:
                raise HTTPException(
                    status_code=global_status,
                    detail=error.dict()
                )
            except Exception as error:
                raise HTTPException(
                    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                    detail=f"An unexpected error occurred. {error}"
                )

        return wrapper

    return decorator
