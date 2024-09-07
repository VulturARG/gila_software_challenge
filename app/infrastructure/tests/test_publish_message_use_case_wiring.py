from unittest import TestCase

from app.application.publish_message_use_case import PublishMessageUseCase
from app.infrastructure.wirings.publish_message_use_case_wiring import PublishMessageUseCaseWiring


class TestPublishMessageUseCaseWiring(TestCase):
    def test_wiring_create_publish_message_use_case_instance(self):
        wiring = PublishMessageUseCaseWiring()
        actual = wiring.instantiate()
        self.assertIsInstance(actual, PublishMessageUseCase)
