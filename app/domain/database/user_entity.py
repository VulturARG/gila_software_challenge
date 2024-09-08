from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Any

from app.domain.notifications.notification_category import NotificationCategory
from app.domain.notifications.notification_channel import NotificationChannel


@dataclass(frozen=True)
class UserEntity:
    id: str
    name: str
    email: str
    phone: str
    channels: list[NotificationChannel]
    subscribed: list[NotificationCategory]

    def as_dict(self) -> dict[str, Any]:
        data = asdict(self)
        data["channels"] = [channel.value for channel in self.channels]
        data["subscribed"] = [subscribed.value for subscribed in self.subscribed]
        return data

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> UserEntity:
        channels = [NotificationChannel(channel) for channel in data["channels"]]
        subscribed = [NotificationCategory(sub) for sub in data["subscribed"]]
        return cls(
            id=data["id"],
            name=data["name"],
            email=data["email"],
            phone=data["phone"],
            channels=channels,
            subscribed=subscribed,
        )
