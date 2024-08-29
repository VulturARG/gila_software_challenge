from app.infrastructure.fastapi.notification_request import NotificationRequest
from fastapi import APIRouter

router = APIRouter()


@router.post("/notification")
async def send_notification(notification: NotificationRequest):
    return {"status": "success", "data": notification}
