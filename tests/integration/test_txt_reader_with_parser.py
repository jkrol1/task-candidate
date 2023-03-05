from typing import Callable

from storage.txt import TxtFileInputParser, TxtFileReader


def test_txt_reader_with_parser(
    open_mock_with_set_read_data: Callable[[str], None]
) -> None:
    parser = TxtFileInputParser()
    expected_parsed_data = [4, 5, 6, 7]
    mocked_file_content = "4,5,6,7"
    open_mock_with_set_read_data(mocked_file_content)
    reader = TxtFileReader()
    data = reader.read("path")
    parsed_data = parser.parse(data)

    assert data == mocked_file_content
    assert parsed_data == expected_parsed_data
