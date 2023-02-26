from enum import Enum
from typing import Type

from algorithm.strategies import SortingStrategy, SubtractionStrategy, IStrategy


class Strategy(Enum):
    SORTING = "sorting"
    SUBTRACTION = "subtraction"

    @classmethod
    def _missing_(cls, name):
        for member in cls:
            if member.name.lower() == name.lower() or member.name.upper() == name.upper():
                return member


StrategyMapping = {Strategy.SORTING: SortingStrategy,
                   Strategy.SUBTRACTION: SubtractionStrategy}


def get_strategy_class(strategy: Strategy) -> Type[IStrategy]:
    return StrategyMapping[strategy]
