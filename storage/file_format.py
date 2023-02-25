from __future__ import annotations

from enum import Enum
import os
from typing import Tuple, Type

from storage.base import IFileReader, IFileWriter
from storage.txt import TxtFileReader, TxtFileWriter


class FileFormat(str, Enum):
    TXT = "txt"

    @staticmethod
    def from_path(path: str) -> FileFormat:
        filename, file_format = os.path.splitext(path)
        file_format = file_format.upper().replace(".", "")
        return FileFormat[file_format]


FileFormatReaderMapping = {FileFormat.TXT: TxtFileReader}
FileFormatWriterMapping = {FileFormat.TXT: TxtFileWriter}


def get_file_reader_and_writer_class_for_given_input_and_output_format(
        input_format: FileFormat, output_format: FileFormat
) -> Tuple[Type[IFileReader], Type[IFileWriter]]:
    reader = FileFormatReaderMapping[input_format]
    writer = FileFormatWriterMapping[output_format]
    return reader, writer
