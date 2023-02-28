from typing import Callable

from algorithm.strategies.base import AlgorithmInput
from storage.base import IFileReader


class TxtFileReader(IFileReader):
    def __init__(self, parsing_function: Callable[[str], AlgorithmInput]):
        self._parsing_function = parsing_function

    def read(self, path: str) -> AlgorithmInput:
        with open(path, "r") as file:
            file_content = file.read()
            return self._parsing_function(file_content)
