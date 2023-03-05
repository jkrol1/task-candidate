import pytest

from algorithm.exceptions import ValidationError
from algorithm.validation import is_algorithm_input_valid


def test_validation() -> None:
    input_data = [1, 2, 3, 4, 5, 6]
    target_sum = 12
    assert is_algorithm_input_valid(input_data, target_sum)


def test_validation_error_for_numbers_less_than_zero_in_input_data() -> None:
    with pytest.raises(ValidationError):
        is_algorithm_input_valid([1, 2, 3, 4, -100], 14)


def test_validation_error_for_numbers_higher_than_target_sum() -> None:
    with pytest.raises(ValidationError):
        is_algorithm_input_valid([1, 2, 3, 4, 100], 14)
