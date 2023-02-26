from typing import List, Set

from algorithm.strategies.base import IStrategy, Result
from input.parser import ParsedData


class BruteForceStrategy(IStrategy):
    def execute(self, data: ParsedData) -> Result:
        result = []
        indexes_of_existing_pairs = set()

        def brute_force(input_list: ParsedData) -> None:
            pair_indexes = self._find_pairs_indexes_in_input_list(
                input_list, indexes_of_existing_pairs
            )

            if not pair_indexes:
                return
            for pair_index in pair_indexes:
                indexes_of_existing_pairs.add(pair_index)

            first_number, second_number = (
                input_list[pair_indexes[0]],
                input_list[pair_indexes[1]],
            )
            result.append([first_number, second_number])
            brute_force(input_list)

        brute_force(data)

        return result

    @staticmethod
    def _find_pairs_indexes_in_input_list(
            input_list: ParsedData, indexes_of_existing_pairs: Set[int]
    ) -> List[int]:
        for idx, value in enumerate(input_list):
            for pair_idx, pair_value in enumerate(input_list[1:], start=1):
                if (
                        value + pair_value == 12
                        and idx not in indexes_of_existing_pairs
                        and pair_idx not in indexes_of_existing_pairs
                ):
                    if value >= pair_value:
                        return [pair_idx, idx]
                    else:
                        return [idx, pair_idx]
