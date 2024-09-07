from dataclasses import asdict, dataclass
from typing import Any

from app.domain.notifications.notification_channel import NotificationChannel


@dataclass(frozen=True)
class UserEntity:
    id: str
    name: str
    email: str
    phone: str
    channels: list[NotificationChannel]

    def as_dict(self) -> dict[str, Any]:
        return asdict(self)
