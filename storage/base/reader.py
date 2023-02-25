from abc import ABC, abstractmethod
from typing import Union


class IFileReader(ABC):
    @abstractmethod
    def read(self, path: str) -> Union[bytes, str]:
        pass
