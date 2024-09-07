from typing import Any
from unittest import TestCase
from unittest.mock import Mock

from app.domain.database.database_repository import DatabaseRepository
from app.domain.database.user_entity import UserEntity
from app.domain.gateways.email_port import EmailPort
from app.domain.gateways.message_dto import UserMessageDTO
from app.domain.gateways.push_notification_port import PushNotificationPort
from app.domain.gateways.sms_port import SmsPort
from app.domain.notifications.notification_category import NotificationCategory
from app.domain.notifications.notification_dto import NotificationDTO
from app.domain.notifications.notification_service import NotificationService
from app.domain.tests.test_doubles.mock_users_table import MOCK_USERS


class TestNotificationService(TestCase):
    def setUp(self):
        self.email_port = Mock(spec=EmailPort)
        self.sms_port = Mock(spec=SmsPort)
        self.push_notification_port = Mock(spec=PushNotificationPort)
        self.user_repository = Mock(spec=DatabaseRepository)
        self.notification = NotificationDTO(
            category=NotificationCategory.FILMS,
            message="Test message",
        )

        self.notification_service = NotificationService(
            email_port=self.email_port,
            sms_port=self.sms_port,
            push_notification_port=self.push_notification_port,
            user_repository=self.user_repository,
        )

    def test_send_notification_by_email(self):
        user = MOCK_USERS["5"]
        user_entity = self._get_user_entity(user)
        self.user_repository.list_subscribed_users.return_value = [user]
        self.notification_service.send_notification(notification=self.notification)

        self.email_port.send.assert_called_once_with(
            message_data=UserMessageDTO(
                message="Test message", user=user_entity
            )
        )

    def test_send_notification_by_sms(self):
        user = MOCK_USERS["2"]
        user_entity = self._get_user_entity(user)
        self.user_repository.list_subscribed_users.return_value = [user]
        self.notification_service.send_notification(notification=self.notification)

        self.sms_port.send.assert_called_once_with(
            message_data=UserMessageDTO(message="Test message", user=user_entity)
        )

    def test_send_notification_by_push(self):
        user = MOCK_USERS["4"]
        user_entity = self._get_user_entity(user)
        self.user_repository.list_subscribed_users.return_value = [user]
        self.notification_service.send_notification(notification=self.notification)

        self.push_notification_port.send.assert_called_once_with(
            message_data=UserMessageDTO(message="Test message", user=user_entity)
        )

    def test_send_notification_by_email_and_push(self):
        user = MOCK_USERS["1"]
        user_entity = self._get_user_entity(user)
        self.user_repository.list_subscribed_users.return_value = [user]
        self.notification_service.send_notification(notification=self.notification)

        self.email_port.send.assert_called_once_with(
            message_data=UserMessageDTO(
                message="Test message", user=user_entity
            )
        )

        self.push_notification_port.send.assert_called_once_with(
            message_data=UserMessageDTO(message="Test message", user=user_entity)
        )

    def test_send_notification_by_all_methods(self):
        user = MOCK_USERS["3"]
        user_entity = self._get_user_entity(user)
        self.user_repository.list_subscribed_users.return_value = [user]
        self.notification_service.send_notification(notification=self.notification)

        self.email_port.send.assert_called_once_with(
            message_data=UserMessageDTO(
                message="Test message", user=user_entity
            )
        )

        self.sms_port.send.assert_called_once_with(
            message_data=UserMessageDTO(message="Test message", user=user_entity)
        )

        self.push_notification_port.send.assert_called_once_with(
            message_data=UserMessageDTO(message="Test message", user=user_entity)
        )

    def _get_user_entity(self, data: dict[str, Any]) -> UserEntity:
        return UserEntity(
            id=data["id"],
            name=data["name"],
            email=data["email"],
            phone=data["phone"],
            channels=data["channels"]
        )
