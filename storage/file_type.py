from __future__ import annotations

import os
from enum import Enum
from typing import Tuple, Type

from storage.base import IFileReader, IFileWriter
from storage.txt import TxtFileReader, TxtFileWriter


class FileType(str, Enum):
    TXT = "txt"

    @staticmethod
    def from_path(path: str) -> FileType:
        filename, file_extension = os.path.splitext(path)
        file_extension = file_extension.upper().replace(".", "")
        return FileType[file_extension]


FileTypeReaderMapping = {FileType.TXT: TxtFileReader}
FileTypeWriterMapping = {FileType.TXT: TxtFileWriter}


def get_reader_and_writer_class_for_given_input_and_output_file_type(
    input_file_type: FileType, output_file_type: FileType
) -> Tuple[Type[IFileReader], Type[IFileWriter]]:
    reader = FileTypeReaderMapping[input_file_type]
    writer = FileTypeWriterMapping[output_file_type]
    return reader, writer
