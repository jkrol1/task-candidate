from output.converter import convert_algorithm_output_to_str


def test_convert_algorithm_output_to_str():
    algorithm_output = [(0, 12), (4, 8)]
    expected_converted_output = "[(0, 12), (4, 8)]"
    converted_output = convert_algorithm_output_to_str(algorithm_output)
    assert converted_output == expected_converted_output
