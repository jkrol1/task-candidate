from typing import Optional, Tuple

from algorithm.strategies import AbstractStrategy, AlgorithmInput, AlgorithmOutput
from algorithm.strategies.base import Pair


class SortingStrategy(AbstractStrategy):
    """
    SortingStrategy algorithm steps:

        1) Sort algorithm input in ascending order
        2) Control search space by using lower_idx and higher_idx.
           At the begging, lower_idx is set to 0 and higher_idx
           is set to the last algorithm input element's index
        3) At each iteration step check if elements at lower_idx and
           higher_idx sum to desired target_sum:

           - If sum of elements equals target_sum then pair is added to
             the found_pairs list, lower_idx is incremented by one and higher_idx
             is decremented by 1
           - If sum of elements is less than target_sum then lower_idx is incremented
             by one
           - If sum of elements is greater than target_sum then higher_idx is
             decremented by one
    """

    def get_pairs(
        self, algorithm_input: AlgorithmInput, target_sum: int
    ) -> AlgorithmOutput:
        found_pairs: AlgorithmOutput = []
        algorithm_input.sort()
        lower_idx, higher_idx = 0, len(algorithm_input) - 1
        while lower_idx < higher_idx:
            pair, lower_idx, higher_idx = self._attempt_to_form_pair(
                lower_idx, higher_idx, algorithm_input, target_sum
            )
            if pair:
                found_pairs.append(pair)
        return found_pairs

    def _attempt_to_form_pair(
        self,
        lower_idx: int,
        higher_idx: int,
        algorithm_input: AlgorithmInput,
        target_sum: int,
    ) -> Tuple[Optional[Pair], int, int]:
        lower_value, higher_value = (
            algorithm_input[lower_idx],
            algorithm_input[higher_idx],
        )
        if lower_value + higher_value == target_sum:
            pair = self.create_pair_from_values(lower_value, higher_value)
            lower_idx += 1
            higher_idx -= 1
            return pair, lower_idx, higher_idx
        elif lower_value + higher_value < target_sum:
            lower_idx += 1
        else:
            higher_idx -= 1

        return None, lower_idx, higher_idx
