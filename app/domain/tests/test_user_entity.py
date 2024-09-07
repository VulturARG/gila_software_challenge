from unittest import TestCase

from app.domain.database.user_entity import UserEntity
from app.domain.gateways.message_dto import UserMessageDTO
from app.domain.notifications.notification_channel import NotificationChannel


class TestUserEntity(TestCase):
    def test_as_dict(self):
        expected = dict(
            id="1",
            name="John Doe",
            email="john.doe@example.com",
            phone="123456789",
            channels=["sms", "email"]
        )

        user = UserEntity(
            id="1",
            name="John Doe",
            email="john.doe@example.com",
            phone="123456789",
            channels=[NotificationChannel.SMS, NotificationChannel.EMAIL]
        )

        actual = user.as_dict()
        self.assertEqual(expected, actual)
