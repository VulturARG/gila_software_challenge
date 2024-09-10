from abc import ABC, abstractmethod

from app.domain.gateways.message_dto import UserMessageDTO


class EmailPort(ABC):
    @abstractmethod
    def send(self, message_data: UserMessageDTO):
        """Sends an email."""
