from algorithm.strategies.base import AlgorithmOutput
from output.converter import convert_algorithm_output_to_str


def test_convert_algorithm_output_to_str() -> None:
    algorithm_output: AlgorithmOutput = [(0, 12), (4, 8)]
    expected_converted_output = "[(0, 12), (4, 8)]"
    converted_output = convert_algorithm_output_to_str(algorithm_output)
    assert converted_output == expected_converted_output
