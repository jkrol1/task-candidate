from abc import ABC, abstractmethod

from algorithm.strategies.base import AlgorithmInput
from input.exceptions import ParserError


class IParser(ABC):
    @abstractmethod
    def parse(self) -> AlgorithmInput:
        pass


class CommaSeparatedInputParser(IParser):
    def __init__(self, input_data: str) -> None:
        self._raw = input_data

    @property
    def raw(self) -> str:
        return self._raw

    def parse(self) -> AlgorithmInput:
        try:
            return [int(value) for value in self._raw.split(",")]
        except ValueError:
            raise ParserError("Values have to be natural numbers separated by comma")
