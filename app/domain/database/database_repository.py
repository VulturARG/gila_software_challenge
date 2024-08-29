from abc import ABC, abstractmethod
from typing import Any


class DatabaseRepository(ABC):
    @abstractmethod
    def create(self, payload: dict[str, Any]) -> dict[str, Any]:
        """Create a register in database table."""

    @abstractmethod
    def delete(self, model_id: str) -> None:
        """Delete a register from database table."""

    @abstractmethod
    def list(self) -> dict[str, Any]:
        """List all register in database table."""

    @abstractmethod
    def retrieve(self, model_id: str) -> dict[str, Any]:
        """Retrieve register from database table."""

    @abstractmethod
    def update(self, model_id: str) -> dict[str, Any]:
        """Update register from database table."""
