from __future__ import annotations

import os
from enum import Enum

from storage.txt import TxtFileReader, TxtFileWriter


class FileType(str, Enum):
    TXT = "txt"

    @staticmethod
    def from_path(path: str) -> FileType:
        filename, file_extension = os.path.splitext(path)
        file_extension = file_extension.lower().replace(".", "")
        return FileType(file_extension)


FileTypeReaderMapping = {FileType.TXT: TxtFileReader}
FileTypeWriterMapping = {FileType.TXT: TxtFileWriter}
