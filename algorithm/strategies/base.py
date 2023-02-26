from abc import ABC, abstractmethod
from typing import List, Optional, Tuple

from input.parser import ParsedData

Pair = Tuple[int, int]
Result = Optional[List[Pair]]


class IStrategy(ABC):
    @abstractmethod
    def get_pairs_from_parsed_data_and_target_sum(
        self, data: ParsedData, target_sum: int
    ) -> Result:
        pass


def create_pair_from_values(first_number: int, second_number: int) -> Pair:
    return (
        (first_number, second_number)
        if first_number < second_number
        else (second_number, first_number)
    )
