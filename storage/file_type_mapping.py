from __future__ import annotations

import os
from dataclasses import dataclass
from enum import Enum
from typing import Type

from storage.base import (
    IAlgorithmOutputConverter,
    IFileInputParser,
    IFileReader,
    IFileWriter,
)
from storage.exceptions import UnsupportedFileType
from storage.txt import (
    AlgorithmOutputToTxtConverter,
    TxtFileInputParser,
    TxtFileReader,
    TxtFileWriter,
)


@dataclass
class ReadHandlers:
    reader: Type[IFileReader]
    parser: Type[IFileInputParser]


@dataclass
class WriteHandlers:
    writer: Type[IFileWriter]
    converter: Type[IAlgorithmOutputConverter]


class FileType(Enum):
    TXT = "txt"

    @classmethod
    def from_path(cls, path: str) -> FileType:
        """
        Get Enum member based on file path.

        :param str path: File path
        :return: FileType member
        :rtype: Filetype
        """

        file_extension = cls._get_file_extension_from_path(path)
        try:
            file_type = cls(file_extension)
            return file_type
        except ValueError:
            raise UnsupportedFileType(f"{file_extension} is not supported")

    @staticmethod
    def _get_file_extension_from_path(path: str) -> str:
        filename, file_extension = os.path.splitext(path)
        file_extension = file_extension.lower().replace(".", "")
        return file_extension


FileTypeToReadHandlersMapping = {
    FileType.TXT: ReadHandlers(reader=TxtFileReader, parser=TxtFileInputParser)
}
FileTypeToWriteHandlersMapping = {
    FileType.TXT: WriteHandlers(
        writer=TxtFileWriter, converter=AlgorithmOutputToTxtConverter
    )
}
