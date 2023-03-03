from abc import ABC, abstractmethod
from typing import List, Optional, Tuple

Pair = Tuple[int, int]
AlgorithmInput = List[int]
AlgorithmOutput = List[Optional[Pair]]


class IStrategy(ABC):
    """Strategy Interface"""

    @abstractmethod
    def get_pairs_from_algorithm_input_and_target_sum(
            self, algorithm_input: AlgorithmInput, target_sum: int
    ) -> AlgorithmOutput:
        """
        Searches for pairs of natural numbers which add up to specified target sum.

        :param AlgorithmInput algorithm_input: Algorithm input
        :param int target_sum: Value to which searched pairs of numbers have to add up
        :return: Found pairs of numbers summing up to `target_sum`
        :rtype: AlgorithmOutput
        """
        pass


def create_pair_from_values(first_number: int, second_number: int) -> Pair:
    """
    Creates properly organized Pair from specified numbers.
    Number at index 0 has to be less than or equal to the number at index 1.

    :param first_number:
    :param second_number:
    :return: Pair of numbers
    :rtype: Pair
    """

    return (
        (first_number, second_number)
        if first_number < second_number
        else (second_number, first_number)
    )
