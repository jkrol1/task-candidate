from enum import Enum

from algorithm.strategies import SortingStrategy, SubtractionStrategy


class BaseEnum(Enum):
    @classmethod
    def values_to_list(cls):
        return list(map(lambda c: c.value, cls))

    @classmethod
    def _missing_(cls, name):
        for member in cls:
            if (
                member.name.lower() == name.lower()
                or member.name.upper() == name.upper()
            ):
                return member


class Strategy(BaseEnum):
    SORTING = "sorting"
    SUBTRACTION = "subtraction"


StrategyMapping = {
    Strategy.SORTING: SortingStrategy,
    Strategy.SUBTRACTION: SubtractionStrategy,
}
