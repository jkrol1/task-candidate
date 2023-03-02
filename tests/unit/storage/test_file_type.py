import pytest

from storage.exceptions import UnsupportedFileType
from storage.file_type_mapping import FileType


def test_from_path_method_with_unsupported_file_type() -> None:
    with pytest.raises(UnsupportedFileType):
        FileType.from_path("test.x")


def test_from_path_method_with_txt_file_type() -> None:
    txt_file_type = FileType.from_path("test.txt")
    assert txt_file_type == FileType.TXT
