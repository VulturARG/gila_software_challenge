from unittest import TestCase
from unittest.mock import Mock

from app.application.publish_message_use_case import PublishMessageUseCase
from app.domain.gateways.file_port import FilePort
from app.infrastructure.tests.test_doubles.mock_file_port import MockFilePort
from app.infrastructure.tests.test_doubles.publish_message_use_case_wiring_for_test import \
    PublishMessageUseCaseWiringForTest


class TestPublishMessageUseCaseWiring(TestCase):
    def setUp(self):
        self.wiring = PublishMessageUseCaseWiringForTest()

    def test_wiring_create_publish_message_use_case_instance(self):
        actual = self.wiring.instantiate()
        self.assertIsInstance(actual, PublishMessageUseCase)

    def test_get_file_gateway_as_mock(self):
        actual = self.wiring.get_file_gateway()
        self.assertIsInstance(actual, Mock)

    def test_override_file_gateway_with_file_port(self):
        actual = self.wiring.get_file_gateway()
        self.assertIsInstance(actual, Mock)

        self.wiring.override_file_gateway(file_gateway=MockFilePort())

        actual = self.wiring.get_file_gateway()
        self.assertIsInstance(actual, FilePort)


