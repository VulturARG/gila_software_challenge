from datetime import datetime
from json import dumps
from unittest import TestCase
from unittest.mock import Mock, patch

from app.domain.gateways.message_dto import UserMessageDTO
from app.domain.logs.log_port import LogPort
from app.domain.logs.log_service import LogService
from app.domain.notifications.notification_channel import NotificationChannel


@patch("app.domain.logs.log_service.datetime")
class TestLogService(TestCase):

    def setUp(self):
        self.expected = {
            "user": {
                "id": "1",
                "name": "John Doe",
                "email": "john.doe@example.com",
                "phone": "123456789",
                "channels": ["sms"],
            },
            "message": "Test message",
        }

        self.mock_log_port = Mock(spec=LogPort)
        self.log_service = LogService(self.mock_log_port)
        self.mock_user_message = Mock(spec=UserMessageDTO)
        self.mock_user_message.as_dict.return_value = self.expected

    def test_info_logs_correct_message(self, mock_datetime: Mock):
        mock_now = datetime(2024, 9, 7, 14, 30, 0)
        mock_datetime.now.return_value = mock_now

        self.log_service.info(
            channel=NotificationChannel.SMS, message_data=self.mock_user_message
        )

        self.mock_user_message.as_dict.assert_called_once()

        expected_message = self.mock_user_message.as_dict()
        expected_message["datetime"] = mock_now.strftime("%Y-%m-%d %H:%M:%S")
        self.mock_log_port.info.assert_called_once_with(
            log_data=dumps(expected_message)
        )

    def test_info_logs_in_json_format(self, mock_datetime: Mock):
        mock_now = datetime(2024, 9, 7, 14, 30, 0)
        mock_datetime.now.return_value = mock_now
        self.expected["datetime"] = mock_now.strftime("%Y-%m-%d %H:%M:%S")
        self.expected["channel"] = "sms"
        expected = dumps(self.expected)

        self.log_service.info(
            channel=NotificationChannel.SMS, message_data=self.mock_user_message
        )

        logged_message = self.mock_log_port.info.call_args[1]["log_data"]
        self.assertTrue(isinstance(logged_message, str))
        self.assertTrue(logged_message.startswith("{") and logged_message.endswith("}"))

        self.assertEqual(expected, logged_message)
