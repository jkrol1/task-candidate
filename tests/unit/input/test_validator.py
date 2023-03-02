import pytest

from input.validator import Validator
from input.exceptions import ValidationError


def test_validator() -> None:
    input_data = [1, 2, 3, 4, 5, 6]
    target_sum = 12
    validator = Validator(input_data, target_sum)
    validator.validate()


def test_validation_error_for_numbers_less_than_zero_in_input_data() -> None:
    validator = Validator([1, 2, 3, 4, -100], 14)
    with pytest.raises(ValidationError):
        validator.validate()


def test_validation_error_for_numbers_higher_than_target_sum() -> None:
    validator = Validator([1, 2, 3, 4, 100], 14)
    with pytest.raises(ValidationError):
        validator.validate()
