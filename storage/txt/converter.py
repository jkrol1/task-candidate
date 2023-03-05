from algorithm.strategies import AlgorithmOutput
from storage.base import IAlgorithmOutputConverter


class AlgorithmOutputToTxtConverter(IAlgorithmOutputConverter[str]):
    def convert(self, algorithm_output: AlgorithmOutput) -> str:
        return str(algorithm_output)
