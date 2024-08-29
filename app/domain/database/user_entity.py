from dataclasses import dataclass

from app.domain.notifications.notification_channel import NotificationChannel


@dataclass(frozen=True)
class UserEntity:
    id: str
    name: str
    email: str
    phone: str
    channels: list[NotificationChannel]
