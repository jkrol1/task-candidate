from typing import Dict

from algorithm.strategies.base import (
    AlgorithmInput,
    AlgorithmOutput,
    IStrategy,
    create_pair_from_values,
)


class SubtractionStrategy(IStrategy):
    def get_pairs_from_algorithm_input_and_target_sum(
        self, algorithm_input: AlgorithmInput, target_sum: int
    ) -> AlgorithmOutput:
        found_pairs: AlgorithmOutput = []
        used_indexes = set()
        value_idx_mapping: Dict[int, int] = {}
        for idx, value in enumerate(algorithm_input):
            pair_candidate_idx = value_idx_mapping.get(target_sum - value)
            if pair_candidate_idx and pair_candidate_idx not in used_indexes:
                pair_candidate_value = algorithm_input[pair_candidate_idx]
                pair = create_pair_from_values(value, pair_candidate_value)
                found_pairs.append(pair)
                used_indexes.add(pair_candidate_idx)
                used_indexes.add(idx)
            value_idx_mapping[value] = idx
        return found_pairs
