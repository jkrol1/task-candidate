from abc import ABC, abstractmethod
from typing import Generic

from algorithm.strategies.base import AlgorithmInput
from storage.base.type import IOType


class IFileInputParser(ABC, Generic[IOType]):
    """FileInputParser Interface."""

    @abstractmethod
    def parse(self, data: IOType) -> AlgorithmInput:
        """
        Parses file content and returns `AlgorithmInput`

        :param str data: File contents
        :return: Algorithm input
        :rtype: AlgorithmInput
        """
        pass
