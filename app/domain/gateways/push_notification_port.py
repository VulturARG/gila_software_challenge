from abc import ABC, abstractmethod

from app.domain.gateways.message_dto import UserMessageDTO


class PushNotificationPort(ABC):
    @abstractmethod
    def send(self, message_data: UserMessageDTO):
        """Sends a Push Notification message."""
