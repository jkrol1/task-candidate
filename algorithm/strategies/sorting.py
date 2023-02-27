from algorithm.strategies.base import IStrategy, AlgorithmInput, AlgorithmOutput, create_pair_from_values


class SortingStrategy(IStrategy):
    def get_pairs_from_parsed_data_and_target_sum(
        self, algorithm_input: AlgorithmInput, sum_target: int
    ) -> AlgorithmOutput:
        found_pairs = []
        algorithm_input.sort()
        lower_idx, higher_idx = 0, len(algorithm_input) - 1
        while lower_idx < higher_idx:
            lower_value, higher_value = algorithm_input[lower_idx], algorithm_input[higher_idx]
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
