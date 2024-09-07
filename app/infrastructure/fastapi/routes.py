from app.domain.notifications.notification_category import NotificationCategory
from app.domain.notifications.notification_dto import NotificationDTO
from app.infrastructure.fastapi.notification_request import NotificationRequest
from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

from app.infrastructure.wirings.publish_message_use_case_wiring import PublishMessageUseCaseWiring

router = APIRouter()


@router.post("/notification", status_code=status.HTTP_202_ACCEPTED)
async def send_notification(notification: NotificationRequest):
    notification_dto = NotificationDTO(
        category=NotificationCategory(notification.category),
        message=notification.message,
    )
    publish_message_use_case = PublishMessageUseCaseWiring().instantiate()
    publish_message_use_case.publish(notification=notification_dto)
    return JSONResponse(
        content={"status": "Notification received", "data": notification.model_dump()},
        status_code=status.HTTP_202_ACCEPTED
    )
