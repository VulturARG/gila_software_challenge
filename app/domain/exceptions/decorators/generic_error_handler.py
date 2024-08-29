import sys
import traceback
from logging import getLogger
from typing import Optional

from app.domain.exceptions.app_base_error import AppBaseWarning, AppBaseError, AppGenericError, AppRequestError

logger = getLogger(__name__)


def generic_error_handler(func):
    def wrapper(*args, **kwargs):
        try:
            class_name = args[0].__class__.__name__
        except IndexError:
            class_name = None
        method_name = func.__name__
        try:
            return func(*args, **kwargs)
        except (AppBaseWarning, AppRequestError) as exc:
            raise exc
        except AppBaseError as exc:
            if not exc.was_error_logged:
                base_exception_logger(
                    class_name=class_name, method_name=method_name, exception=exc
                )
                exc.was_error_logged = True
            raise exc
        except Exception as exc:
            logger_error_details(
                exc=exc, method_name=method_name, class_name=class_name
            )
            error = AppGenericError(exc)
            error.was_error_logged = True
            raise error from exc

    return wrapper


def logger_error_details(
    exc: Exception, method_name: str, class_name: Optional[str]
) -> None:
    tb = traceback.extract_tb(sys.exc_info()[2])
    _, line_number, _, _ = tb[-1]

    if class_name is None:
        logger.error(
            "ERROR: '%s' exception was raised in line %s in '%s' function/method.",
            exc.__class__.__name__,
            line_number,
            method_name,
        )
        return None

    logger.error(
        "ERROR: '%s' exception was raised in line %s in '%s' method of the '%s' class.",
        exc.__class__.__name__,
        line_number,
        method_name,
        class_name,
    )
    logger.exception("Unhandled exception")


def base_exception_logger(
    class_name: str, method_name: str, exception: AppBaseError
) -> None:
    logger_error_details(exc=exception, method_name=method_name, class_name=class_name)
    message = exception.dict().get("error", "No error message received")
    logger.exception("ERROR MESSAGE: %s", message)
