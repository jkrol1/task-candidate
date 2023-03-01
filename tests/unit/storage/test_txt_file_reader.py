from storage.txt import TxtFileReader


def test_read(mocker, open_mock):
    algorithm_input = [4, 5, 6, 7]
    parsing_function_input = "4;5;6;7"
    parsing_function = mocker.MagicMock(return_value=algorithm_input)
    open_mock(parsing_function_input)
    reader = TxtFileReader(parsing_function)
    data = reader.read("path")

    parsing_function.assert_called_once_with(parsing_function_input)
    assert data == algorithm_input
