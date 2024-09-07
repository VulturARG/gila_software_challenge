from app.domain.gateways.file_port import FilePort


class MockFilePort(FilePort):
    def __init__(self):
        self.in_memory_storage = []

    def read(self, file_path: str) -> list[str]:
        return self.in_memory_storage

    def write(self, file_path: str, content: str) -> None:
        self.in_memory_storage.append(content)
