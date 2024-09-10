from app.domain.exceptions.app_base_error import AppRequestError


class DatabaseError(AppRequestError):
    """Base class for all exceptions in this module."""


class IdNotFoundError(DatabaseError):
    def __init__(self, table: str, record_id: str) -> None:
        self.MESSAGE = f"{table.capitalize()} with ID {record_id} not found"
        super().__init__(self.MESSAGE)
