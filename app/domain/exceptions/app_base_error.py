from typing import Any, Dict, Optional


class AppBaseError(Exception):
    """Base class for all own exceptions."""

    MESSAGE: Optional[str] = None
    was_error_logged: bool = False

    def dict(self) -> Dict[str, str]:
        """Return error message as dict"""

        default_message = f"The '{self.__class__.__name__}' base class should not be used to raise exceptions."
        message = self.MESSAGE if self.MESSAGE is not None else default_message
        return {"error": message}


class AppGenericError(AppBaseError):
    def __init__(
        self,
        exception_or_message: Any,
    ) -> None:
        super().__init__()

        msg = (
            type(exception_or_message)
            if isinstance(exception_or_message, Exception)
            and not isinstance(exception_or_message, AppBaseError)
            else exception_or_message
        )
        self._exception_or_message = str(msg)

    def dict(self):
        return {"generic error": self._exception_or_message}


class AppBaseWarning(AppBaseError):
    """Base class for all own warnings."""


class AppRequestError(AppBaseError):
    """Base class for all own request errors."""


