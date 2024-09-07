from unittest.mock import Mock

from app.domain.gateways.file_port import FilePort
from app.infrastructure.wirings.publish_message_use_case_wiring import (
    PublishMessageUseCaseWiring,
)


class PublishMessageUseCaseWiringForTest(PublishMessageUseCaseWiring):
    def __init__(self):
        self._file_gateway_adapter = Mock(spec=FilePort)

    def get_file_gateway(self) -> Mock or FilePort:
        """Allows the tests to set the return value of the mock."""
        return self._file_gateway_adapter

    def override_file_gateway(self, file_gateway: FilePort) -> None:
        """The user may want to replace it with a double for testing."""
        self._file_gateway_adapter = file_gateway

    def _file_port(self) -> FilePort:
        """Overrides the base class method."""
        return self._file_gateway_adapter
