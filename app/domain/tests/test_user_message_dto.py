from unittest import TestCase

from app.domain.database.user_entity import UserEntity
from app.domain.gateways.message_dto import UserMessageDTO
from app.domain.notifications.notification_category import NotificationCategory
from app.domain.notifications.notification_channel import NotificationChannel


class TestUserMessageDto(TestCase):
    def test_as_dict(self):
        expected = dict(
            user=dict(
                id="1",
                name="John Doe",
                email="john.doe@example.com",
                phone="123456789",
                channels=["sms", "email"],
                subscribed=["films"],
            ),
            message="Hello, World!",
        )

        user = UserEntity(
            id="1",
            name="John Doe",
            email="john.doe@example.com",
            phone="123456789",
            channels=[NotificationChannel.SMS, NotificationChannel.EMAIL],
            subscribed=[NotificationCategory.FILMS],
        )

        dto = UserMessageDTO(user=user, message="Hello, World!")
        actual = dto.as_dict()
        self.assertEqual(expected, actual)
