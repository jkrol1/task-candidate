from argparse import ArgumentParser


def create_parser() -> ArgumentParser:
    parser = ArgumentParser(
        description="Application for finding pairs of natural numbers which add up to 12"
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
    return parser
