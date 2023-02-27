from typing import Dict

from algorithm.strategies.base import IStrategy, AlgorithmInput, AlgorithmOutput, create_pair_from_values


class SubtractionStrategy(IStrategy):
    def get_pairs_from_parsed_data_and_target_sum(
            self, algorithm_input: AlgorithmInput, sum_target: int
    ) -> AlgorithmOutput:
        found_pairs = []
        used_indexes = set()
        value_idx_mapping: Dict[int, int] = {}
        for idx, value in enumerate(algorithm_input):
            pair_candidate_idx = value_idx_mapping.get(sum_target - value)
            if pair_candidate_idx and pair_candidate_idx not in used_indexes:
                pair_candidate_value = algorithm_input[pair_candidate_idx]
                pair = create_pair_from_values(value, pair_candidate_value)
                found_pairs.append(pair)
                used_indexes.add(pair_candidate_idx)
                used_indexes.add(idx)
            value_idx_mapping[value] = idx
        return found_pairs
