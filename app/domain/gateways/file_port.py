from abc import ABC, abstractmethod
from typing import Any


class FilePort(ABC):
    """I/O File Gateway Port."""

    @abstractmethod
    def read(self, file_path: str) -> list[dict[str, Any]]:
        """Read the contents of the file."""

    @abstractmethod
    def write(self, file_path: str, content: str) -> None:
        """Write the content to a file."""
