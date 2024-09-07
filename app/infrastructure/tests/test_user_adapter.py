from unittest import TestCase

from app.infrastructure.adapters.database.user_adapter import UsersAdapter
from app.infrastructure.tests.test_doubles.mock_orm import MockORM
from app.infrastructure.tests.test_doubles.mock_subscribed_table import (
    MOCK_SUBSCRIBED_QUERY,
)


class TestUserAdapter(TestCase):
    def setUp(self):
        self.orm = MockORM()
        self.expected = MOCK_SUBSCRIBED_QUERY["sports"]

    def test_page_size_is_none(self):
        user_adapter = UsersAdapter(orm=self.orm, page_size=None)
        actual = list(user_adapter.list_subscribed_users(category="sports"))
        self.assertEqual(self.expected, actual)

    def test_page_size_is_grater_than_total_records(self):
        user_adapter = UsersAdapter(orm=self.orm, page_size=100)
        actual = list(user_adapter.list_subscribed_users(category="sports"))
        self.assertEqual(self.expected, actual)

    def test_page_size_is_less_than_total_records_and_is_not_multiple_of_total_record(
        self,
    ):
        user_adapter = UsersAdapter(orm=self.orm, page_size=2)
        actual = list(user_adapter.list_subscribed_users(category="sports"))
        self.assertEqual(self.expected, actual)
