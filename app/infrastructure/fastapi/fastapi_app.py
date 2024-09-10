from app.domain.exceptions.app_base_error import (
    AppBaseError,
    AppBaseWarning,
    AppGenericError,
    AppRequestError,
)
from app.domain.notifications.notification_category import NotificationCategory
from app.domain.notifications.notification_dto import NotificationDTO
from app.infrastructure.fastapi.notification_request import NotificationRequest
from app.infrastructure.wirings.publish_message_use_case_wiring import (
    PublishMessageUseCaseWiring,
)
from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse

app = FastAPI()


@app.exception_handler(AppBaseWarning)
async def app_base_warning_handler(request: Request, exc: AppBaseWarning):
    return JSONResponse(
        status_code=status.HTTP_202_ACCEPTED,
        content={"detail": exc.dict()},
    )


@app.exception_handler(AppRequestError)
async def app_request_error_handler(request: Request, exc: AppRequestError):
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={"detail": exc.dict()},
    )


@app.exception_handler(AppGenericError)
async def app_generic_error_handler(request: Request, exc: AppGenericError):
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={"detail": exc.dict()},
    )


@app.exception_handler(AppBaseError)
async def app_base_error_handler(request: Request, exc: AppBaseError):
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={"detail": exc.dict()},
    )


@app.post("/notification", status_code=status.HTTP_202_ACCEPTED)
async def send_notification(notification: NotificationRequest):
    notification_dto = NotificationDTO(
        category=NotificationCategory(notification.category),
        message=notification.message,
    )
    publish_message_use_case = PublishMessageUseCaseWiring().instantiate()
    publish_message_use_case.publish(notification=notification_dto)
    return JSONResponse(
        content={"status": "Notification received", "data": notification.model_dump()},
        status_code=status.HTTP_202_ACCEPTED,
    )
