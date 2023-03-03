from __future__ import annotations

from enum import Enum
from typing import List, Any, Optional

from algorithm.strategies import SortingStrategy, SubtractionStrategy


class BaseEnum(Enum):
    @classmethod
    def values_to_list(cls) -> List[Any]:
        """
        Creates list from Enum's values

        :return: List of Enum's values
        :rtype: List[Any]
        """

        return [e.value for e in cls]

    @classmethod
    def _missing_(cls, name) -> Optional[BaseEnum]:
        for member in cls:
            if (
                    member.name.lower() == name.lower()
                    or member.name.upper() == name.upper()
            ):
                return member

        return None


class Strategy(BaseEnum):
    SORTING = "sorting"
    SUBTRACTION = "subtraction"


StrategyMapping = {
    Strategy.SORTING: SortingStrategy,
    Strategy.SUBTRACTION: SubtractionStrategy,
}
