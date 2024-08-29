
from fastapi import APIRouter

from app.infrastructure.fastapi.notification_request import NotificationRequest
from app.infrastructure.fastapi.router_handle_exceptions import handle_exceptions

router = APIRouter()


@router.post("/notification")
@handle_exceptions()
async def send_notification(notification: NotificationRequest):
    return {"status": "success", "data": notification}
