from enum import Enum


class NotificationChannel(str, Enum):
    SMS = "sms"
    EMAIL = "email"
    PUSH = "push_notification"
