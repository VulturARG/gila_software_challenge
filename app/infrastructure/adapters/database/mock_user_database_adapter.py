from typing import Any

from app.domain.database.database_errors import IdNotFoundError
from app.domain.database.database_repository import DatabaseRepository
from app.infrastructure.adapters.database.mock_users_table import MOCK_USERS


class MockUsersTable(DatabaseRepository):
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
        except KeyError:
            raise IdNotFoundError(table="user", record_id=model_id)

    def update(self, model_id: str) -> dict[str, Any]:
        """Update register from database table."""
