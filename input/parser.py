from algorithm.strategies.base import AlgorithmInput
from input.exceptions import ParserError


def parse_comma_separated_input_data(input_data: str) -> AlgorithmInput:
    try:
        return [int(value) for value in input_data.split(",")]
    except ValueError:
        raise ParserError("Values have to be natural numbers separated by comma")
