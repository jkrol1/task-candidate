from unittest.mock import MagicMock

from pytest_mock import MockFixture

from algorithm.strategies.base import AlgorithmOutput
from storage.txt import TxtFileWriter


def test_write(mocker: MockFixture, open_mock: MagicMock) -> None:
    algorithm_output: AlgorithmOutput = [(2, 10), (0, 12)]
    converted_algorithm_output = str(algorithm_output)
    converter_function = mocker.MagicMock(return_value=converted_algorithm_output)
    writer = TxtFileWriter(converter_function)
    writer.write("path", algorithm_output)

    open_mock().write.assert_called_once_with(converted_algorithm_output)
