from abc import ABC, abstractmethod


class SmsPort(ABC):
    @abstractmethod
    def send(self):
        """Sends a SMS message."""
