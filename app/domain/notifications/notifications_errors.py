from app.domain.exceptions.app_base_error import AppRequestError


class NotificationError(AppRequestError):
    """Base class for all exceptions in this module."""


class NotificationRequestError(NotificationError):
    def __init__(self, message) -> None:
        self.MESSAGE = message
        super().__init__(self.MESSAGE)
