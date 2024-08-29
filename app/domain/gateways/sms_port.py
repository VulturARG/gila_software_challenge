from abc import ABC, abstractmethod

from app.domain.gateways.message_dto import MessageDTO


class SmsPort(ABC):
    @abstractmethod
    def send(self, message_data: MessageDTO):
        """Sends a SMS message."""
