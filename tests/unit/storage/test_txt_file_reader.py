from typing import Callable

from storage.txt import TxtFileReader


def test_read(open_mock_with_set_read_data: Callable[[str], None]) -> None:
    mocked_file_content = "4;5;6;7"
    open_mock_with_set_read_data(mocked_file_content)
    reader = TxtFileReader()
    data = reader.read("path")

    assert data == mocked_file_content
