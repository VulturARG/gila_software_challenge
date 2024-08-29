from abc import ABC, abstractmethod


class EmailPort(ABC):
    @abstractmethod
    def send(self):
        """Sends an email."""
