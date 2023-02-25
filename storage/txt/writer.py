from typing import Union

from storage.base import IFileWriter


class TxtFileWriter(IFileWriter):
    def write(self, path: str, data: Union[str, bytes]) -> None:
        with open(path, "w") as file:
            file.write(data)
