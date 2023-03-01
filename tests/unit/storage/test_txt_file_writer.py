from storage.txt import TxtFileWriter


def test_write(mocker, open_mock):
    algorithm_output = [(2, 10), (0, 12)]
    converted_algorithm_output = str(algorithm_output)
    converter_function = mocker.MagicMock(return_value=converted_algorithm_output)
    writer = TxtFileWriter(converter_function)
    writer.write("path", algorithm_output)

    open_mock().write.assert_called_once_with(converted_algorithm_output)
