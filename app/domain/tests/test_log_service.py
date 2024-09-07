import unittest
from unittest.mock import Mock
from datetime import datetime
from app.domain.logs.log_port import LogPort
from app.domain.gateways.message_dto import UserMessageDTO
from json import dumps

from app.domain.logs.log_service import LogService


class TestLogService(unittest.TestCase):

    def setUp(self):
        self.mock_log_port = Mock(spec=LogPort)
        self.log_service = LogService(self.mock_log_port)
        self.mock_user_message = Mock(spec=UserMessageDTO)
        self.mock_user_message.as_dict.return_value = {
            "user": {
                "id": "1",
                "name": "John Doe",
                "email": "john.doe@example.com",
                "phone": "123456789",
                "channels": ["sms", "email"],
            },
            "message": "Test message",
        }

    def test_info_logs_correct_message(self):
        self.log_service.info(self.mock_user_message)

        self.mock_user_message.as_dict.assert_called_once()

        current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        expected = self.mock_user_message.as_dict()
        expected["datetime"] = current_datetime

        self.mock_log_port.info.assert_called_once_with(log_data=dumps(expected))

    def test_info_logs_in_json_format(self):
        self.log_service.info(self.mock_user_message)

        logged_message = self.mock_log_port.info.call_args[1]["log_data"]
        self.assertTrue(isinstance(logged_message, str))
        self.assertTrue(logged_message.startswith("{") and logged_message.endswith("}"))
