import pytest

from input.parser import parse_comma_separated_input_data
from input.exceptions import ParserError


def test_parse_comma_separated_input_data():
    input_data = "1,2,3,4,5,6,7"
    expected_parsed_data = [1, 2, 3, 4, 5, 6, 7]
    parsed_data = parse_comma_separated_input_data(input_data)
    assert parsed_data == expected_parsed_data


def test_parse_comma_separated_input_data_with_incorrect_delimiter():
    input_data = "1@2@3@4@5"
    with pytest.raises(ParserError):
        parse_comma_separated_input_data(input_data)
