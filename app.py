from __future__ import annotations

from argparse import Namespace
from dataclasses import dataclass

from algorithm.strategies import IStrategy
from algorithm.strategy_mapping import Strategy, StrategyMapping
from input.parser import parse_comma_separated_input_data
from input.validator import Validator
from output.converter import convert_algorithm_output_to_str
from storage.base import IFileReader, IFileWriter
from storage.file_type_mapping import (FileType, FileTypeReaderMapping,
                                       FileTypeWriterMapping)


@dataclass
class Context:
    input_file_path: str
    input_file_type: FileType
    output_file_path: str
    output_file_type: FileType
    strategy: Strategy
    target_sum: int

    @classmethod
    def from_parsed_cli_args(cls, parsed_args: Namespace) -> Context:
        input_file_type = FileType.from_path(parsed_args.input_file_path)
        output_file_type = FileType.from_path(parsed_args.output_file_path)
        strategy = Strategy(parsed_args.strategy)
        context = cls(
            input_file_path=parsed_args.input_file_path,
            input_file_type=input_file_type,
            output_file_path=parsed_args.output_file_path,
            output_file_type=output_file_type,
            target_sum=parsed_args.target_sum,
            strategy=strategy,
        )
        return context


class App:
    def __init__(
        self,
        reader: IFileReader,
        writer: IFileWriter,
        context: Context,
        strategy: IStrategy,
    ) -> None:
        self._reader = reader
        self._writer = writer
        self._context = context
        self._strategy = strategy

    def run(self) -> None:
        algorithm_input = self._reader.read(self._context.input_file_path)
        Validator(algorithm_input, self._context.target_sum).validate()
        algorithm_output = self._strategy.get_pairs_from_algorithm_input_and_target_sum(
            algorithm_input, self._context.target_sum
        )
        self._writer.write(self._context.output_file_path, algorithm_output)


def create_app(context: Context) -> App:
    reader = FileTypeReaderMapping[context.input_file_type]
    writer = FileTypeWriterMapping[context.output_file_type]
    strategy = StrategyMapping[context.strategy]

    app = App(
        reader=reader(parsing_function=parse_comma_separated_input_data),
        writer=writer(converting_function=convert_algorithm_output_to_str),
        context=context,
        strategy=strategy(),
    )

    return app
