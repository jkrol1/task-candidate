from storage.base import IFileWriter


class TxtFileWriter(IFileWriter[str]):
    def write(self, path: str, converted_data: str) -> None:
        with open(path, "w") as file:
            file.write(converted_data)
