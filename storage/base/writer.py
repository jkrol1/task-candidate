from abc import ABC, abstractmethod

from algorithm.strategies.base import AlgorithmOutput


class IFileWriter(ABC):
    @abstractmethod
    def write(self, path: str, data: AlgorithmOutput) -> None:
        pass
