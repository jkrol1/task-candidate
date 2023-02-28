from abc import ABC, abstractmethod

from algorithm.strategies.base import AlgorithmInput


class IFileReader(ABC):
    @abstractmethod
    def read(self, path: str) -> AlgorithmInput:
        pass
