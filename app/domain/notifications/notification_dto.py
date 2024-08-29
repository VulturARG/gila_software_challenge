from dataclasses import dataclass

from app.domain.notifications.notification_category import NotificationCategory


@dataclass(frozen=True)
class NotificationDTO:
    category: NotificationCategory
    message: str
