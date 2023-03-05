from storage.base import IFileReader


class TxtFileReader(IFileReader[str]):
    def read(self, path: str) -> str:
        with open(path, "r") as file:
            file_content = file.read()
            return file_content
