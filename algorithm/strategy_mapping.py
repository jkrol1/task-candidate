from enum import Enum

from algorithm.strategies import SortingStrategy, SubtractionStrategy


class Strategy(Enum):
    SORTING = "sorting"
    SUBTRACTION = "subtraction"

    @classmethod
    def _missing_(cls, name):
        for member in cls:
            if (
                member.name.lower() == name.lower()
                or member.name.upper() == name.upper()
            ):
                return member


StrategyMapping = {
    Strategy.SORTING: SortingStrategy,
    Strategy.SUBTRACTION: SubtractionStrategy,
}
