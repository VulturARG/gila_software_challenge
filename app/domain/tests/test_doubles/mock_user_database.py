from typing import Any, List, Optional

from app.domain.database.database_errors import IdNotFoundError
from app.domain.database.database_repository import DatabaseRepository
from app.domain.tests.test_doubles.mock_subscribed_table import MOCK_SUBSCRIBED
from app.domain.tests.test_doubles.mock_users_table import MOCK_USERS


class MockUsersTable(DatabaseRepository):
    def __init__(self, offset: Optional[int] = None, page_size: Optional[int] = None):
        self._offset = offset
        self._page_size = page_size

    def create(self, payload: dict[str, Any]) -> dict[str, Any]:
        """Create a register in database table."""

    def delete(self, model_id: str) -> None:
        """Delete a register from database table."""

    def list(self) -> dict[str, Any]:
        """List all register in database table."""

    def retrieve(self, model_id: str) -> dict[str, Any]:
        """Retrieve register from database table."""
        try:
            return MOCK_USERS[model_id]
        except KeyError as error:
            raise IdNotFoundError(table="user", record_id=model_id) from error

    def update(self, model_id: str) -> dict[str, Any]:
        """Update register from database table."""

    def list_subscribed_users(self, category: str) -> List[dict[str, Any]]:
        """Retrieve users from subscribed."""
        return self._mock_list_subscribed_users(category=category)

    def count_subscribed_users(self, category: str) -> int:
        """Count users from subscribed."""
        return len(MOCK_SUBSCRIBED.get(category, []))

    def _mock_list_subscribed_users(self, category: str) -> List[dict[str, Any]]:
        """Mock list subscribed users."""
        if self._offset is None or self._page_size is None:
            return MOCK_SUBSCRIBED.get(category, [])
        return MOCK_SUBSCRIBED[category][self._offset:self._offset + self._page_size]
