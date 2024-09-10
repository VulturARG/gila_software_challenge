from datetime import datetime
from json import dumps

from app.domain.gateways.message_dto import UserMessageDTO
from app.domain.logs.log_port import LogPort
from app.domain.notifications.notification_channel import NotificationChannel


class LogService:
    def __init__(self, log_port: LogPort):
        self._logger = log_port

    def info(self, channel: NotificationChannel, message_data: UserMessageDTO):
        """Info a log message."""
        message = message_data.as_dict()
        message_datetime = datetime.now()
        message["datetime"] = message_datetime.strftime("%Y-%m-%d %H:%M:%S")
        message["channel"] = channel.value

        self._logger.info(log_data=dumps(message))
