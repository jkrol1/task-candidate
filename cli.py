from argparse import Action, ArgumentParser

from config import STRATEGIES, DEFAULT_STRATEGY, DEFAULT_TARGET_SUM


class TargetSumAction(Action):
    def __call__(self, parser, namespace, values, option_string=None):
        argument = "/".join(self.option_strings)
        try:
            int_value = int(values)
            if int_value < 0:
                parser.error(
                    f"argument {argument}: invalid value: '{int_value}'. Target sum has to be >= 0"
                )
            setattr(namespace, self.dest, int_value)
        except ValueError:
            parser.error(f"argument {argument}: invalid int value: '{values}'")


def create_cli_parser() -> ArgumentParser:
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
        default=DEFAULT_STRATEGY,
        const=DEFAULT_STRATEGY,
        nargs="?",
        choices=STRATEGIES,
        help="Strategy used for finding pairs of natural numbers which add up to specified target sum",
    )
    parser.add_argument(
        "-t",
        "--target-sum",
        action=TargetSumAction,
        default=DEFAULT_TARGET_SUM,
        nargs="?",
        const=DEFAULT_TARGET_SUM,
        help="Target sum value of pairs",
    )
    return parser
