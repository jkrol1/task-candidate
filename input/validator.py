from abc import ABC, abstractmethod

from input.exceptions import ValidationError
from input.parser import ParsedData


class IValidator(ABC):
    @abstractmethod
    def validate(self) -> None:
        pass


class Validator(IValidator):
    def __init__(self, parsed_data: ParsedData) -> None:
        self._parsed_data = parsed_data

    def validate(self) -> None:
        for number in self._parsed_data:
            if not 0 <= number <= 12:
                raise ValidationError(f"Number {number} is not in allowed threshold")
