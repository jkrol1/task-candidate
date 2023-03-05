from unittest.mock import MagicMock

from storage.txt import TxtFileWriter


def test_write(open_mock: MagicMock) -> None:
    converted_algorithm_output = "[(2, 10), (0, 12)]"
    path = "path"
    writer = TxtFileWriter()
    writer.write(path, converted_algorithm_output)

    open_mock().write.assert_called_once_with(converted_algorithm_output)
