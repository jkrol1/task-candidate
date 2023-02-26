from algorithm.strategies.base import IStrategy, Result, create_pair_from_values
from input.parser import ParsedData


class SortingStrategy(IStrategy):
    def get_pairs_from_given_data_and_target_sum(
        self, data: ParsedData, sum_target: int
    ) -> Result:
        found_pairs = []
        data.sort()
        lower_idx, higher_idx = 0, len(data) - 1
        while lower_idx < higher_idx:
            lower_value, higher_value = data[lower_idx], data[higher_idx]
            if lower_value + higher_value == sum_target:
                pair = create_pair_from_values(lower_value, higher_value)
                found_pairs.append(pair)
                lower_idx += 1
                higher_idx -= 1
            elif lower_value + higher_value < sum_target:
                lower_idx += 1
            else:
                higher_idx -= 1
        return found_pairs
