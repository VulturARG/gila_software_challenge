from app.domain.gateways.file_port import FilePort
from app.domain.logs.log_port import LogPort


class LogAdapter(LogPort):
    def __init__(self, file_port: FilePort, file_path: str):
        self._file_port = file_port
        self._file_path = file_path

    def info(self, log_data: str) -> None:
        """Store a log message."""
        self._file_port.write(file_path=self._file_path, content=log_data)
