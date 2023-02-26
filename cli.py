from argparse import ArgumentParser


def create_parser() -> ArgumentParser:
    parser = ArgumentParser(
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
