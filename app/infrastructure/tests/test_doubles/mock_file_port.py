from app.domain.gateways.file_port import FilePort


class MockFilePort(FilePort):
    def __init__(self, in_memory_storage: list[str]):
        self._in_memory_storage = in_memory_storage

    def read(self, file_path: str) -> list[str]:
        return self._in_memory_storage

    def write(self, file_path: str, content: str) -> None:
        self._in_memory_storage.append(content)
