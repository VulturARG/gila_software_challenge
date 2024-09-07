from app.domain.gateways.message_dto import UserMessageDTO
from app.domain.gateways.sms_port import SmsPort
from app.domain.logs.log_service import LogService


class SmsAdapter(SmsPort):
    def __init__(self, log_service: LogService):
        self._log_service = log_service

    def send(self, message_data: UserMessageDTO):
        """Sends a SMS message."""
        self._log_service.info(message_data=message_data)
