from abc import ABC, abstractmethod

from algorithm.strategies.base import AlgorithmOutput


class IFileWriter(ABC):
    """FileWriter Interface"""

    @abstractmethod
    def write(self, path: str, data: AlgorithmOutput) -> None:
        """
        Write algorithm output to file in specified path

        :param str path: File path
        :param AlgorithmOutput data: Algorithm output
        :return:
        """
        pass
