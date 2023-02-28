from abc import ABC, abstractmethod

from algorithm.strategies.base import AlgorithmInput
from input.exceptions import ValidationError


class IValidator(ABC):
    @abstractmethod
    def validate(self) -> None:
        pass


class Validator(IValidator):
    def __init__(self, algorithm_input: AlgorithmInput, target_sum: int) -> None:
        self._algorithm_input = algorithm_input
        self._target_sum = target_sum

    def validate(self) -> None:
        self._validate_target_sum()
        self._validate_algorithm_input()

    def _validate_algorithm_input(self) -> None:
        for number in self._algorithm_input:
            if not 0 <= number <= self._target_sum:
                raise ValidationError(f"Number {number} is not in allowed threshold")

    def _validate_target_sum(self) -> None:
        if self._target_sum < 0:
            raise ValidationError(f"Invalid target sum {self._target_sum}. It has to be a natural number")
