from abc import ABC, abstractmethod
from typing import List, Optional


class IStrategy(ABC):
    @abstractmethod
    def execute(self, data: List[int]) -> Optional[List[List[int, int]]]:
        pass
