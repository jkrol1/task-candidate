from abc import ABC, abstractmethod
from typing import Generic

from storage.base.type import IOType


class IFileWriter(ABC, Generic[IOType]):
    """FileWriter Interface."""

    @abstractmethod
    def write(self, path: str, data: IOType) -> None:
        """
        Write algorithm output to file in specified path.

        :param str path: File path
        :param AlgorithmOutput data: Algorithm output
        :return:
        """
        pass
