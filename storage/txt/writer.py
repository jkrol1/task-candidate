from typing import Callable

from algorithm.strategies.base import AlgorithmOutput
from storage.base import IFileWriter


class TxtFileWriter(IFileWriter):
    def __init__(self, converting_function: Callable[[AlgorithmOutput], str]) -> None:
        self._converting_function = converting_function

    def write(self, path: str, data: AlgorithmOutput) -> None:
        with open(path, "w") as file:
            converted_algorithm_output = self._converting_function(data)
            file.write(converted_algorithm_output)
