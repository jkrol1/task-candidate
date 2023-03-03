import pytest

from algorithm.strategies import SortingStrategy, SubtractionStrategy
from algorithm.strategies.base import AlgorithmInput, AlgorithmOutput

SUBTRACTION_STRATEGY_ALGORITHM_INPUT_OUTPUT_TARGET_SUM = [
    (
        [4, 8, 9, 0, 12, 1, 4, 2, 12, 12, 4, 4, 8, 11, 12, 0],
        [(4, 8), (0, 12), (4, 8), (1, 11), (0, 12)],
        12
    ),
    (
        [7, 5, 3, 4, 9, 11, 6, 4, 12, 12, 9, 8, 7, 7, 3, 1],
        [(5, 9), (3, 11), (6, 8), (7, 7)],
        14
    ),
    (
        [9, 15, 5, 12, 20, 0, 9, 7, 6, 14, 5, 9, 12, 8, 0, 7, 3, 8, 15, 14, 6],
        [(5, 15), (0, 20), (6, 14), (8, 12), (5, 15), (6, 14)],
        20
    ),
    (
        [14, 14, 5, 12, 20, 0, 9, 7, 6, 22, 5, 20, 12, 9, 9, 9, 9, 9, 7, 7, 2, 3, 1, 4, 5, 18, 0, 0, 0],
        [(12, 12), (2, 22), (4, 20), (6, 18)],
        24
    ),
    (
        [14, 14, 5, 12, 20, 0, 9, 7, 6, 22, 5, 20, 12, 9, 9, 9, 9, 9, 7, 7, 2, 3, 1, 4, 5, 18, 0, 0, 0],
        [],
        100
    ),
]

SORTING_STRATEGY_ALGORITHM_INPUT_OUTPUT_TARGET_SUM = [
    (
        [4, 8, 9, 0, 12, 1, 4, 2, 12, 12, 4, 4, 8, 11, 12, 0],
        [(0, 12), (0, 12), (1, 11), (4, 8), (4, 8)],
        12
    ),
    (
        [7, 5, 3, 4, 9, 11, 6, 4, 12, 12, 9, 8, 7, 7, 3, 1],
        [(3, 11), (5, 9), (6, 8), (7, 7)],
        14
    ),
    (
        [9, 15, 5, 12, 20, 0, 9, 7, 6, 14, 5, 9, 12, 8, 0, 7, 3, 8, 15, 14, 6],
        [(0, 20), (5, 15), (5, 15), (6, 14), (6, 14), (8, 12), (8, 12)],
        20
    ),
    (
        [14, 14, 5, 12, 20, 0, 9, 7, 6, 22, 5, 20, 12, 9, 9, 9, 9, 9, 7, 7, 2, 3, 1, 4, 5, 18, 0, 0, 0],
        [(2, 22), (4, 20), (6, 18), (12, 12)],
        24
    ),
    (
        [14, 14, 5, 12, 20, 0, 9, 7, 6, 22, 5, 20, 12, 9, 9, 9, 9, 9, 7, 7, 2, 3, 1, 4, 5, 18, 0, 0, 0],
        [],
        100
    ),
]


@pytest.mark.parametrize("algorithm_input, expected_algorithm_output, target_sum",
                         SUBTRACTION_STRATEGY_ALGORITHM_INPUT_OUTPUT_TARGET_SUM)
def test_subtraction_strategy(algorithm_input: AlgorithmInput, expected_algorithm_output: AlgorithmOutput,
                              target_sum: int) -> None:
    strategy = SubtractionStrategy()
    algorithm_output = strategy.get_pairs_from_algorithm_input_and_target_sum(algorithm_input, target_sum)

    assert algorithm_output == expected_algorithm_output


@pytest.mark.parametrize("algorithm_input, expected_algorithm_output, target_sum",
                         SORTING_STRATEGY_ALGORITHM_INPUT_OUTPUT_TARGET_SUM)
def test_sorting_strategy(algorithm_input: AlgorithmInput, expected_algorithm_output: AlgorithmOutput,
                          target_sum: int) -> None:
    strategy = SortingStrategy()
    algorithm_output = strategy.get_pairs_from_algorithm_input_and_target_sum(algorithm_input, target_sum)

    assert algorithm_output == expected_algorithm_output
