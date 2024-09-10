from app.domain.gateways.file_port import FilePort


class FileGatewayAdapter(FilePort):
    """I/O File Gateway adapter."""

    def read(self, file_path: str) -> str:
        """Read the contents of the file."""
        with open(file_path, "r") as file:
            return file.read()

    def write(self, file_path: str, content: str) -> None:
        """Write the content to a file."""
        with open(file_path, "a") as file:
            file.write(f"{content}\n")
