from app.domain.gateways.message_dto import UserMessageDTO
from app.domain.gateways.push_notification_port import PushNotificationPort
from app.domain.logs.log_service import LogService


class PushNotificationAdapter(PushNotificationPort):
    def __init__(self, log_service: LogService):
        self._log_service = log_service

    def send(self, message_data: UserMessageDTO):
        """Sends a Push Notification message."""
        self._log_service.info(message_data=message_data)
