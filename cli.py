from argparse import Action, ArgumentParser, Namespace
from typing import Optional, Sequence, Union

from config import DEFAULT_STRATEGY, DEFAULT_TARGET_SUM, STRATEGIES


class TargetSumAction(Action):
    """Custom action for parsing target sum argument from CLI."""

    def __call__(
        self,
        parser: ArgumentParser,
        namespace: Namespace,
        values: Union[str, Sequence, None],
        option_string: Optional[str] = None,
    ) -> None:
        target_sum = self._get_target_sum_from_values_or_raise_parser_error(
            values, parser
        )
        setattr(namespace, self.dest, target_sum)

    def _get_target_sum_from_values_or_raise_parser_error(self, values, parser):
        argument = "/".join(self.option_strings)
        try:
            target_sum = int(values)
            if target_sum < 0:
                parser.error(
                    f"argument {argument}: invalid value: '{target_sum}'. Target sum has to be >= 0"
                )
            return target_sum
        except ValueError:
            parser.error(f"argument {argument}: invalid int value: '{values}'")


def create_cli_parser() -> ArgumentParser:
    """
    ArgumentParser factory.

    :return: CLI argument parser
    :rtype: ArgumentParser
    """

    parser = ArgumentParser(
        description="Application for finding pairs of natural numbers which add up to specified target sum"
    )
    parser.add_argument(
        "-i",
        "--input-file-path",
        help="File path to application's input. "
        "Input has to be in .txt format and it has to consist of natural numbers separated by comma",
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
