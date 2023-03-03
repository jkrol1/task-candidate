from argparse import ArgumentParser
from typing import List

import pytest
from _pytest.capture import CaptureFixture

from config import DEFAULT_STRATEGY, DEFAULT_TARGET_SUM

ARGS_EXPECTED_ERROR_MSG = [
    (
        ["-t", "15"],
        "the following arguments are required: -i/--input-file-path, -o/--output-file-path",
    ),
    (
        ["-t", "15", "-s", "dummy"],
        "argument -s/--strategy: invalid choice: 'dummy' (choose from 'sorting', 'subtraction')",
    ),
    (["-t", "dummy"], "argument -t/--target-sum: invalid int value: 'dummy'"),
    (["-t", "10.5"], "argument -t/--target-sum: invalid int value: '10.5'"),
    (
        ["-t", "-5"],
        "argument -t/--target-sum: invalid value: '-5'. Target sum has to be >= 0",
    ),
]


def test_create_cli_parser(cli_parser: ArgumentParser) -> None:
    expected_description = "Application for finding pairs of natural numbers which add up to specified target sum"

    assert isinstance(cli_parser, ArgumentParser)
    assert cli_parser.description == expected_description


@pytest.mark.parametrize("args, expected_error_msg", ARGS_EXPECTED_ERROR_MSG)
def test_cli_parser_with_invalid_args_input(
    args: List[str],
    expected_error_msg: str,
    cli_parser: ArgumentParser,
    capsys: CaptureFixture[str],
) -> None:
    try:
        cli_parser.parse_args(args)
    except SystemExit:
        pass

    captured = capsys.readouterr()

    assert expected_error_msg in captured.err


def test_cli_parser(cli_parser: ArgumentParser) -> None:
    input_file_path = "input_file.txt"
    output_file_path = "output_file.txt"
    strategy = "sorting"
    target_sum = "15"
    parsed_args = cli_parser.parse_args(
        [
            "-i",
            input_file_path,
            "-o",
            output_file_path,
            "-s",
            strategy,
            "-t",
            target_sum,
        ]
    )

    assert parsed_args.input_file_path == input_file_path
    assert parsed_args.output_file_path == output_file_path
    assert parsed_args.strategy == strategy
    assert parsed_args.target_sum == int(target_sum)


def test_cli_parser_default_args(cli_parser: ArgumentParser) -> None:
    parsed_args = cli_parser.parse_args(["-i", "test.txt", "-o", "test_output.txt"])

    assert parsed_args.strategy == DEFAULT_STRATEGY
    assert parsed_args.target_sum == DEFAULT_TARGET_SUM
