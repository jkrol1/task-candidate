from storage.txt import TxtFileReader


def test_read(mocker, open_mock_with_read_data):
    algorithm_input = [4, 5, 6, 7]
    mocked_file_content = "4;5;6;7"
    parsing_function = mocker.MagicMock(return_value=algorithm_input)
    open_mock_with_read_data(mocked_file_content)
    reader = TxtFileReader(parsing_function)
    data = reader.read("path")

    parsing_function.assert_called_once_with(mocked_file_content)
    assert data == algorithm_input
