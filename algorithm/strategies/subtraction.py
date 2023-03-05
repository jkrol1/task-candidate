from typing import Dict

from algorithm.strategies import AbstractStrategy, AlgorithmInput, AlgorithmOutput


class SubtractionDictStrategy(AbstractStrategy):
    """
    SubtractionDictStrategy algorithm steps:

        1) At each iteration step over algorithm input, values
           are added to the value_idx_mapping dictionary which maps
           values to their indexes in original algorithm input list.
        2) Check if value of difference between target_sum and current iteration
           value already exists in the value_idx_mapping dictionary. If it
           exists and was not used to form a pair, then new pair is formed
           and appended to the found_pairs list
    """

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
