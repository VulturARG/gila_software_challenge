from abc import ABC, abstractmethod


class LogPort(ABC):
    @abstractmethod
    def info(self, log_data: str) -> None:
        """Store a log message."""
