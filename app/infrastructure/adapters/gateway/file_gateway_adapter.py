from app.domain.gateways.file_port import FilePort


class FileGatewayAdapter(FilePort):
    """I/O File Gateway adapter."""

    def read(self, file_path_name: str) -> str:
        """Read the contents of the file."""
        with open(file_path_name, "r") as file:
            return file.read()

    def write(self, file_path_name: str, content: str) -> None:
        """Write the content to a file."""
        with open(file_path_name, "w") as file:
            file.write(content)
