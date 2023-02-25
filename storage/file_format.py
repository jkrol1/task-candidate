from enum import Enum
from typing import Tuple, Type

from storage.base import IFileReader, IFileWriter
from storage.txt import TxtFileReader, TxtFileWriter


class FileFormat(str, Enum):
    TXT = "txt"


FileFormatReaderMapping = {FileFormat.TXT: TxtFileReader}
FileFormatWriterMapping = {FileFormat.TXT: TxtFileWriter}


def get_file_reader_and_writer_class_for_given_input_and_output_format(
    input_format: FileFormat, output_format: FileFormat
) -> Tuple[Type[IFileReader], Type[IFileWriter]]:
    reader = FileFormatReaderMapping[input_format]
    writer = FileFormatWriterMapping[output_format]
    return reader, writer
