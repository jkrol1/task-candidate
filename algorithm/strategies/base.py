from abc import ABC, abstractmethod
from typing import List, Optional

from input.parser import ParsedData

Result = Optional[List[List[int]]]


class IStrategy(ABC):
    @abstractmethod
    def execute(self, data: ParsedData) -> Result:
        pass
