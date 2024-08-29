from unittest import TestCase
from unittest.mock import Mock

from app.domain.gateways.email_message_dto import EmailMessageDto
from app.domain.gateways.email_port import EmailPort
from app.domain.gateways.push_message_dto import PushMessageDto
from app.domain.gateways.push_notification_port import PushNotificationPort
from app.domain.gateways.sms_message_dto import SmsMessageDto
from app.domain.gateways.sms_port import SmsPort
from app.domain.notifications.notification_category import NotificationCategory
from app.domain.notifications.notification_dto import NotificationDTO
from app.domain.notifications.notification_service import NotificationService
from app.domain.tests.test_doubles.mock_user_database import MockUsersTable


class TestNotificationService(TestCase):
    def setUp(self):
        self.email_port = Mock(spec=EmailPort)
        self.sms_port = Mock(spec=SmsPort)
        self.push_notification_port = Mock(spec=PushNotificationPort)
        self.subscribed_repository = Mock()
        self.user_repository = MockUsersTable()
        self.notification = NotificationDTO(
            category=NotificationCategory.FILMS,
            message="Test message",
        )

        self.notification_service = NotificationService(
            email_port=self.email_port,
            sms_port=self.sms_port,
            push_notification_port=self.push_notification_port,
            subscribed_repository=self.subscribed_repository,
            user_repository=self.user_repository,
        )

    def test_send_notification_by_email(self):
        self.subscribed_repository.retrieve.return_value = ["5"]
        self.notification_service.send_notification(notification=self.notification)

        self.email_port.send.assert_called_once_with(
            message_data=EmailMessageDto(
                message="Test message", to_email="johndoe@example.com"
            )
        )

    def test_send_notification_by_sms(self):
        self.subscribed_repository.retrieve.return_value = ["2"]
        self.notification_service.send_notification(notification=self.notification)

        self.sms_port.send.assert_called_once_with(
            message_data=SmsMessageDto(message="Test message", phone="234-567-8901")
        )

    def test_send_notification_by_push(self):
        self.subscribed_repository.retrieve.return_value = ["4"]
        self.notification_service.send_notification(notification=self.notification)

        self.push_notification_port.send.assert_called_once_with(
            message_data=PushMessageDto(message="Test message", push_id="4")
        )

    def test_send_notification_by_email_and_push(self):
        self.subscribed_repository.retrieve.return_value = ["1"]
        self.notification_service.send_notification(notification=self.notification)

        self.email_port.send.assert_called_once_with(
            message_data=EmailMessageDto(
                message="Test message", to_email="alice.johnson@example.com"
            )
        )

        self.push_notification_port.send.assert_called_once_with(
            message_data=PushMessageDto(message="Test message", push_id="1")
        )

    def test_send_notification_by_all_methods(self):
        self.subscribed_repository.retrieve.return_value = ["3"]
        self.notification_service.send_notification(notification=self.notification)

        self.email_port.send.assert_called_once_with(
            message_data=EmailMessageDto(
                message="Test message", to_email="charlie.brown@example.com"
            )
        )

        self.sms_port.send.assert_called_once_with(
            message_data=SmsMessageDto(message="Test message", phone="345-678-9012")
        )

        self.push_notification_port.send.assert_called_once_with(
            message_data=PushMessageDto(message="Test message", push_id="3")
        )
