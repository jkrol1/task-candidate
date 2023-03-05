from unittest.mock import MagicMock

from algorithm.strategies import AlgorithmOutput
from storage.txt import AlgorithmOutputToTxtConverter, TxtFileWriter


def test_txt_reader_with_parser(open_mock: MagicMock) -> None:
    converter = AlgorithmOutputToTxtConverter()
    algorithm_output: AlgorithmOutput = [(2, 10), (0, 12)]
    expected_converted_algorithm_output = "[(2, 10), (0, 12)]"
    path = "path"
    writer = TxtFileWriter()
    writer.write(path, converter.convert(algorithm_output))

    open_mock().write.assert_called_once_with(expected_converted_algorithm_output)
