from typing import Any, List, Optional

from app.domain.database.database_repository import DatabaseRepository
from app.infrastructure.tests.test_doubles.mock_orm import MockORM


class UsersAdapter(DatabaseRepository):
    """Users adapter."""

    def __init__(self, orm: MockORM, page_size: Optional[int] = None):
        self.orm = orm
        self._page_size = page_size

    def create(self, payload: dict[str, Any]) -> dict[str, Any]:
        """Create a register in database table."""

    def delete(self, model_id: str) -> None:
        """Delete a register from database table."""

    def list(self) -> dict[str, Any]:
        """List all register in database table."""

    def retrieve(self, model_id: str) -> dict[str, Any]:
        """Retrieve register from database table."""

    def update(self, model_id: str) -> dict[str, Any]:
        """Update register from database table."""

    def count_subscribed_users(self, category: str) -> int:
        """Count users from subscribed."""
        return self.orm.count_subscribed_users(category)

    def list_subscribed_users(self, category: str) -> List[dict[str, Any]]:
        """Retrieve users from subscribed."""
        total_records = self.count_subscribed_users(category=category)
        if self._page_size is None:
            self._page_size = total_records
        for offset in range(0, total_records, self._page_size):
            yield from self.orm.list_subscribed_users(
                category=category, offset=offset, page_size=self._page_size
            )
