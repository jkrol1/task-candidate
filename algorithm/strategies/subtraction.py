from typing import Dict

from algorithm.strategies import AbstractStrategy, AlgorithmInput, AlgorithmOutput


class SubtractionStrategy(AbstractStrategy):
    def get_pairs(
        self, algorithm_input: AlgorithmInput, target_sum: int
    ) -> AlgorithmOutput:
        found_pairs: AlgorithmOutput = []
        used_indexes = set()
        value_idx_mapping: Dict[int, int] = {}
        for idx, value in enumerate(algorithm_input):
            pair_candidate_idx = value_idx_mapping.get(target_sum - value)
            if (
                pair_candidate_idx is not None
                and pair_candidate_idx not in used_indexes
            ):
                pair_candidate_value = algorithm_input[pair_candidate_idx]
                pair = self.create_pair_from_values(value, pair_candidate_value)
                found_pairs.append(pair)
                used_indexes.add(pair_candidate_idx)
                used_indexes.add(idx)
            value_idx_mapping[value] = idx
        return found_pairs
