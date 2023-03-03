from abc import ABC, abstractmethod

from algorithm.strategies.base import AlgorithmInput


class IFileReader(ABC):
    """FileReader Interface"""

    @abstractmethod
    def read(self, path: str) -> AlgorithmInput:
        """
        Reads file from specified path

        :param str path: File path
        :return: Algorithm input
        :rtype: AlgorithmInput
        """
        pass
