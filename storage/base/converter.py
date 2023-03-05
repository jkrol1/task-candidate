from abc import ABC, abstractmethod
from typing import Generic

from algorithm.strategies import AlgorithmOutput
from storage.base.type import IOType


class IAlgorithmOutputConverter(ABC, Generic[IOType]):
    """AlgorithmOutputConverter Interface."""

    @abstractmethod
    def convert(self, algorithm_output: AlgorithmOutput) -> IOType:
        """
        Converts algorithm output into `IOType`

        :param AlgorithmOutput algorithm_output: Algorithm output
        :return: Converted algorithm output
        :rtype: str
        """
        pass
