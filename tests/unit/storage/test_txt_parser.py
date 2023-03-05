import pytest

from storage.exceptions import ParsingError
from storage.txt import TxtFileInputParser


def test_parse_comma_separated_input_data() -> None:
    input_data = "1,2,3,4,5,6,7"
    expected_parsed_data = [1, 2, 3, 4, 5, 6, 7]
    parsed_data = TxtFileInputParser().parse(input_data)
    assert parsed_data == expected_parsed_data


def test_parse_comma_separated_input_data_with_incorrect_delimiter() -> None:
    input_data = "1@2@3@4@5"
    with pytest.raises(ParsingError):
        TxtFileInputParser().parse(input_data)
