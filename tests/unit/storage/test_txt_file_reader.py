from typing import Callable

from pytest_mock import MockFixture

from storage.txt import TxtFileReader


def test_read(
    mocker: MockFixture, open_mock_with_set_read_data: Callable[[str], None]
) -> None:
    algorithm_input = [4, 5, 6, 7]
    mocked_file_content = "4;5;6;7"
    parsing_function = mocker.MagicMock(return_value=algorithm_input)
    open_mock_with_set_read_data(mocked_file_content)
    reader = TxtFileReader(parsing_function)
    data = reader.read("path")

    parsing_function.assert_called_once_with(mocked_file_content)
    assert data == algorithm_input
