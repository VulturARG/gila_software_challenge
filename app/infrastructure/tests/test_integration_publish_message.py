from datetime import datetime
from unittest import TestCase
from unittest.mock import Mock, patch

from app.domain.notifications.notification_category import NotificationCategory
from app.domain.notifications.notification_dto import NotificationDTO
from app.infrastructure.tests.test_doubles.mock_file_port import MockFilePort
from app.infrastructure.tests.test_doubles.mock_log_in_memory import MOCK_LOG_IN_MEMORY
from app.infrastructure.tests.test_doubles.publish_message_use_case_wiring_for_test import (
    PublishMessageUseCaseWiringForTest,
)


class TestIntegrationPublishMessage(TestCase):
    def setUp(self):
        self.storage = []
        self.mock_file_gateway = MockFilePort(in_memory_storage=self.storage)
        self.wiring = PublishMessageUseCaseWiringForTest()
        self.wiring.override_file_gateway(file_gateway=self.mock_file_gateway)
        self.use_case = self.wiring.instantiate()

    @patch("app.domain.logs.log_service.datetime")
    def test_publish_message_type_sports_success(self, mock_datetime: Mock):
        expected = MOCK_LOG_IN_MEMORY
        mock_now = datetime(2024, 9, 7, 14, 30, 0)
        mock_datetime.now.return_value = mock_now

        notification = NotificationDTO(
            category=NotificationCategory.SPORTS,
            message="Test message",
        )
        self.use_case.publish(notification=notification)

        actual = self.mock_file_gateway.read("")
        self.assertEqual(expected, actual)
