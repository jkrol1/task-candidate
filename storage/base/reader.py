from abc import ABC, abstractmethod
from typing import Generic

from storage.base.type import IOType


class IFileReader(ABC, Generic[IOType]):
    """FileReader Interface."""

    @abstractmethod
    def read(self, path: str) -> IOType:
        """
        Reads file from specified path.

        :param str path: File path
        :return: Algorithm input
        :rtype: AlgorithmInput
        """
        pass
