from algorithm.exceptions import ValidationError
from algorithm.strategies import AlgorithmInput


def is_algorithm_input_valid(algorithm_input: AlgorithmInput, target_sum: int) -> bool:
    """
    Validates algorithm input and returns `True` if valid. Raises `ValidationError` on
    validation failure.

    :param AlgorithmInput algorithm_input: Algorithm input
    :param int target_sum: Value to which searched pairs of numbers have to add up
    :return: True if data is valid
    :rtype: bool
    """

    for number in algorithm_input:
        if not 0 <= number <= target_sum:
            raise ValidationError(f"Number {number} is not in allowed threshold")
    return True
