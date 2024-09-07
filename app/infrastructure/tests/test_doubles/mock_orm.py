from typing import Any, List, Optional

from app.infrastructure.tests.test_doubles.mock_subscribed_table import (
    MOCK_SUBSCRIBED_QUERY,
)


class MockORM:

    def count_subscribed_users(self, category: str) -> int:
        """Count users from subscribed."""
        return len(MOCK_SUBSCRIBED_QUERY.get(category, []))

    def list_subscribed_users(
        self, category: str, offset: int, page_size: Optional[int] = None
    ) -> List[dict[str, Any]]:
        """Mock list subscribed users."""
        if page_size is None:
            return MOCK_SUBSCRIBED_QUERY.get(category, [])
        return MOCK_SUBSCRIBED_QUERY[category][offset : offset + page_size]
