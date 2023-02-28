from argparse import ArgumentParser

from algorithm.strategy_mapping import Strategy
from app import Context
from storage.file_type_mapping import FileType


class AppArgumentParser(ArgumentParser):
    def create_app_context(self) -> Context:
        parsed_args = self.parse_args()
        input_file_type = FileType.from_path(parsed_args.input_file_path)
        output_file_type = FileType.from_path(parsed_args.output_file_path)
        strategy = Strategy(parsed_args.strategy)
        context = Context(
            input_file_path=parsed_args.input_file_path,
            input_file_type=input_file_type,
            output_file_path=parsed_args.output_file_path,
            output_file_type=output_file_type,
            target_sum=parsed_args.target_sum,
            strategy=strategy,
        )
        return context


def create_cli_parser() -> AppArgumentParser:
    parser = AppArgumentParser(
        description="Application for finding pairs of natural numbers which add up to specified target sum"
    )
    parser.add_argument(
        "-i",
        "--input-file-path",
        help="File path to application's input",
        required=True,
    )
    parser.add_argument(
        "-o",
        "--output-file-path",
        help="File path to application's output",
        required=True,
    )
    parser.add_argument(
        "-s",
        "--strategy",
        default="subtraction",
        const="subtraction",
        nargs="?",
        choices=["subtraction", "sorting"],
        help="Strategy used for finding pairs of natural numbers which add up to specified target sum",
    )
    parser.add_argument(
        "-t",
        "--target-sum",
        default=12,
        nargs="?",
        const=12,
        type=int,
        help="Target sum value of pairs",
    )
    return parser
