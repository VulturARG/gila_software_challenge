from app.domain.gateways.email_port import EmailPort
from app.domain.gateways.message_dto import UserMessageDTO
from app.domain.logs.log_service import LogService
from app.domain.notifications.notification_channel import NotificationChannel


class EmailAdapter(EmailPort):
    def __init__(self, log_service: LogService):
        self._log_service = log_service

    def send(self, message_data: UserMessageDTO):
        """Sends an email."""
        self._log_service.info(
            channel=NotificationChannel.EMAIL, message_data=message_data
        )
