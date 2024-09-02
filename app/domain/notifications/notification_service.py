from typing import Iterable, Any

from app.domain.database.database_repository import DatabaseRepository
from app.domain.database.user_entity import UserEntity
from app.domain.gateways.email_port import EmailPort
from app.domain.gateways.message_dto import UserMessageDTO
from app.domain.gateways.push_notification_port import PushNotificationPort
from app.domain.gateways.sms_port import SmsPort
from app.domain.notifications.notification_channel import NotificationChannel
from app.domain.notifications.notification_dto import NotificationDTO


class NotificationService:
    def __init__(
        self,
        email_port: EmailPort,
        sms_port: SmsPort,
        push_notification_port: PushNotificationPort,
        user_repository: DatabaseRepository,
    ):
        self.email_port = email_port
        self.sms_port = sms_port
        self.push_notification_port = push_notification_port
        self.user_repository = user_repository

    def send_notification(self, notification: NotificationDTO) -> None:
        raw_users = self.user_repository.list_subscribed_users(category=notification.category.value,)
        users = self._list_users_to_notify(users=raw_users)

        for user in users:
            self._send_to_user(notification.message, user)

    def _list_users_to_notify(self, users: list[dict[str, Any]]) -> Iterable[UserEntity]:
        for user in users:
            yield UserEntity(
                id=user["id"],
                name=user["name"],
                email=user["email"],
                phone=user["phone"],
                channels=self._notification_channels(user["channels"]),
            )

    def _notification_channels(self, channels: list[str]) -> list[NotificationChannel]:
        return [self._channel_map()[channel] for channel in channels]

    def _channel_map(self) -> dict[str, NotificationChannel]:
        return {
            "sms": NotificationChannel.SMS,
            "email": NotificationChannel.EMAIL,
            "push_notification": NotificationChannel.PUSH,
        }

    def _send_to_user(self, message: str, user: UserEntity) -> None:
        for channel in user.channels:
            if channel == NotificationChannel.EMAIL:
                message_data = UserMessageDTO(message=message, user=user)
                self.email_port.send(message_data=message_data)
            if channel == NotificationChannel.SMS:
                message_data = UserMessageDTO(message=message, user=user)
                self.sms_port.send(message_data=message_data)
            if channel == NotificationChannel.PUSH:
                message_data = UserMessageDTO(message=message, user=user)
                self.push_notification_port.send(message_data=message_data)
