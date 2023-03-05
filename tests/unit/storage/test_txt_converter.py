from algorithm.strategies import AlgorithmOutput
from storage.txt import AlgorithmOutputToTxtConverter


def test_convert_algorithm_output_to_str() -> None:
    algorithm_output: AlgorithmOutput = [(0, 12), (4, 8)]
    expected_converted_output = "[(0, 12), (4, 8)]"
    converted_output = AlgorithmOutputToTxtConverter().convert(algorithm_output)

    assert converted_output == expected_converted_output
