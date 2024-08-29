from abc import ABC, abstractmethod


class LogPort(ABC):
    @abstractmethod
    def store(self):
        """Store a log message."""
