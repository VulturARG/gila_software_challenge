from abc import ABC, abstractmethod
from typing import Any


class NonSqlDatabaseRepository(ABC):
    @abstractmethod
    def mock_find_subscribed_users(self, category: str) -> list[dict[str, Any]]:
        """Retrieve users from subscribed."""
