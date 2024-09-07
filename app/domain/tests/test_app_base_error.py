from unittest import TestCase

from app.domain.exceptions.app_base_error import AppBaseError, AppGenericError


class TestAppBaseError(TestCase):

    def test_dict_returns_default_message(self):
        expected = {
            "error": "The 'AppBaseError' base class should not be used to raise exceptions."
        }
        error = AppBaseError()
        actual = error.dict()
        self.assertEqual(expected, actual)

    def test_dict_returns_custom_message(self):
        class CustomError(AppBaseError):
            MESSAGE = "Custom error occurred"

        expected = {"error": "Custom error occurred"}
        error = CustomError()
        actual = error.dict()

        self.assertEqual(expected, actual)

    def test_initialization_with_exception(self):
        expected = {'generic error': "<class 'ValueError'>"}
        try:
            raise ValueError("Test exception")
        except ValueError as e:
            error = AppGenericError(e)

        actual = error.dict()
        self.assertEqual(expected, actual)

    def test_initialization_with_message(self):
        expected = {'generic error': 'Test message'}
        error = AppGenericError("Test message")
        actual = error.dict()
        self.assertEqual(expected, actual)



