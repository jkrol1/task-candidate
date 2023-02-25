from abc import ABC, abstractmethod
from typing import Union


class IFileWriter(ABC):
    @abstractmethod
    def write(self, path: str, data: Union[str, bytes]) -> None:
        pass
