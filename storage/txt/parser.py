from algorithm.strategies import AlgorithmInput
from storage.base import IFileInputParser
from storage.exceptions import ParsingError


class TxtFileInputParser(IFileInputParser[str]):
    def parse(self, data: str) -> AlgorithmInput:
        try:
            return [int(value) for value in data.split(",")]
        except ValueError:
            raise ParsingError(
                "Input values have to be natural numbers separated by comma"
            )
