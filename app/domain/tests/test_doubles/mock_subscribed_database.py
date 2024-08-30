from typing import Any

from app.domain.database.non_sql_database_repository import NonSqlDatabaseRepository
from app.domain.tests.test_doubles.mock_subscribed_table import SUBSCRIBED


class MockSubscribedTable(NonSqlDatabaseRepository):
    def mock_find_subscribed_users(self, category: str) -> list[dict[str, Any]]:
        """Retrieve users from subscribed."""
        return SUBSCRIBED.get(category, [])
