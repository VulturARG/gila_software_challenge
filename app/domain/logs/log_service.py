from app.domain.logs.log_port import LogPort
from app.domain.gateways.message_dto import UserMessageDTO
from datetime import datetime
from json import dumps


class LogService:
    def __init__(self, log_port: LogPort):
        self._logger = log_port

    def info(self, message_data: UserMessageDTO):
        """Info a log message."""
        message = message_data.as_dict()
        message_datetime = datetime.now()
        message["datetime"] = message_datetime.strftime("%Y-%m-%d %H:%M:%S")

        self._logger.info(log_data=dumps(message))
