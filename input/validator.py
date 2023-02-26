from abc import ABC, abstractmethod

from input.exceptions import ValidationError
from input.parser import ParsedData


class IValidator(ABC):
    @abstractmethod
    def validate(self) -> None:
        pass


class Validator(IValidator):
    def __init__(self, parsed_data: ParsedData, target_sum: int) -> None:
        self._parsed_data = parsed_data
        self._target_sum = target_sum

    def validate(self) -> None:
        for number in self._parsed_data:
            if not 0 <= number <= self._target_sum:
                raise ValidationError(f"Number {number} is not in allowed threshold")
