from storage.base import IFileReader


class TxtFileReader(IFileReader):
    def read(self, path: str) -> str:
        with open(path, "r") as file:
            return file.read()
