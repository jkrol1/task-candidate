from algorithm.strategy_mapping import Strategy
from app import Context
from config import DEFAULT_STRATEGY, DEFAULT_TARGET_SUM
from storage.file_type_mapping import FileType


def test_create_context_from_parsed_cli_args(cli_parser):
    input_file_path = "input.txt"
    output_file_path = "output.txt"
    parsed_cli_args = cli_parser.parse_args(["-i", input_file_path, "-o", output_file_path])
    context = Context.from_parsed_cli_args(parsed_cli_args)

    assert context.input_file_path == input_file_path
    assert context.input_file_type == FileType.TXT
    assert context.output_file_path == output_file_path
    assert context.output_file_type == FileType.TXT
    assert context.strategy == Strategy(DEFAULT_STRATEGY)
    assert context.target_sum == DEFAULT_TARGET_SUM
