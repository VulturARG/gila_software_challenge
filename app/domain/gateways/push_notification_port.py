from abc import ABC, abstractmethod


class PushNotificationPort(ABC):
    @abstractmethod
    def send(self):
        """Sends a Push Notification message."""
