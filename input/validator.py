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
        for number in self._algorithm_input:
            if not 0 <= number <= self._target_sum:
                raise ValidationError(f"Number {number} is not in allowed threshold")
