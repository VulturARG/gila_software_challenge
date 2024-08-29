from abc import ABC, abstractmethod

from app.domain.gateways.message_dto import MessageDTO


class PushNotificationPort(ABC):
    @abstractmethod
    def send(self, message_data: MessageDTO):
        """Sends a Push Notification message."""
