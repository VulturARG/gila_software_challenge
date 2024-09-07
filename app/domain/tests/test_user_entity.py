from unittest import TestCase

from app.domain.database.user_entity import UserEntity
from app.domain.notifications.notification_category import NotificationCategory
from app.domain.notifications.notification_channel import NotificationChannel


class TestUserEntity(TestCase):
    def test_as_dict(self):
        expected = dict(
            id="1",
            name="John Doe",
            email="john.doe@example.com",
            phone="123456789",
            channels=["sms", "email"],
            subscribed=["films", "finance"],
        )

        user = UserEntity(
            id="1",
            name="John Doe",
            email="john.doe@example.com",
            phone="123456789",
            channels=[NotificationChannel.SMS, NotificationChannel.EMAIL],
            subscribed=[NotificationCategory.FILMS, NotificationCategory.FINANCE]
        )

        actual = user.as_dict()
        self.assertEqual(expected, actual)

    def test_from_dict(self):
        expected = UserEntity(
            id="1",
            name="John Doe",
            email="john.doe@example.com",
            phone="123456789",
            channels=[NotificationChannel.SMS, NotificationChannel.EMAIL],
            subscribed=[NotificationCategory.FILMS, NotificationCategory.FINANCE]
        )

        user = dict(
            id="1",
            name="John Doe",
            email="john.doe@example.com",
            phone="123456789",
            channels=["sms", "email"],
            subscribed=["films", "finance"],
        )
        actual = UserEntity.from_dict(user)
        self.assertEqual(expected, actual)

