import unittest

from app.domain.notifications.notifications_errors import NotificationRequestError
from app.infrastructure.fastapi.notification_request import NotificationRequest


class TestNotificationRequest(unittest.TestCase):
    def test_valid_request(self):
        expected = "A valid message"
        request = NotificationRequest(category="sports", message="A valid message")
        self.assertEqual(request.category, "sports")
        self.assertEqual(expected, request.message)

    def test_invalid_category(self):
        with self.assertRaises(NotificationRequestError):
            NotificationRequest(category="InvalidCategory", message="A valid message")


