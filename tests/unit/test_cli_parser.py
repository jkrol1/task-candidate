import pytest

from argparse import ArgumentParser
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


def test_create_cli_parser(cli_parser):
    expected_description = "Application for finding pairs of natural numbers which add up to specified target sum"

    assert isinstance(cli_parser, ArgumentParser)
    assert cli_parser.description == expected_description


@pytest.mark.parametrize("args, expected_error_msg", ARGS_EXPECTED_ERROR_MSG)
def test_cli_parser_with_invalid_args_input(
        args, expected_error_msg, cli_parser, capsys
):
    try:
        cli_parser.parse_args(args)
    except SystemExit:
        pass

    captured = capsys.readouterr()

    assert expected_error_msg in captured.err


def test_cli_parser(cli_parser):
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


def test_cli_parser_default_args(cli_parser):
    parsed_args = cli_parser.parse_args(
        ["-i", "test.txt", "-o", "test_output.txt"]
    )

    assert parsed_args.strategy == DEFAULT_STRATEGY
    assert parsed_args.target_sum == DEFAULT_TARGET_SUM
