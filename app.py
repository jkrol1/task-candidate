from __future__ import annotations

from argparse import Namespace
from dataclasses import dataclass

from algorithm.strategies import AbstractStrategy
from algorithm.strategy_mapping import Strategy, StrategyMapping
from algorithm.validation import is_algorithm_input_valid
from storage.base import (
    IAlgorithmOutputConverter,
    IFileInputParser,
    IFileReader,
    IFileWriter,
)
from storage.file_type_mapping import (
    FileType,
    FileTypeToReadHandlersMapping,
    FileTypeToWriteHandlersMapping,
)


@dataclass
class Context:
    """
    Application context.

    :param input_file_path: Path to input file
    :param FileType input_file_type: Member of FileType enum representing input file type
    :param str output_file_path: Path to output file
    :param FileType output_file_type: Member of FileType enum representing output file type
    :param Strategy strategy: Member of Strategy enum representing chosen calculation strategy
    :param int target_sum: Value to which searched pairs of numbers have to add up
    """

    input_file_path: str
    input_file_type: FileType
    output_file_path: str
    output_file_type: FileType
    strategy: Strategy
    target_sum: int

    @classmethod
    def from_parsed_cli_args(cls, parsed_args: Namespace) -> Context:
        """
        Creates Context from parsed CLI Arguments.

        :param Namespace parsed_args: Parsed CLI arguments
        :return: Application context
        :rtype: Context
        """

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
    """
    Application controller class.

    :param IFileReader reader: Concrete reader responsible for reading input file
    :param IFileInputParser parser: File content parser
    :param IAlgorithmOutputConverter converter: Converts algorithm output into writable format
    :param IFileWriter writer: Concrete writer responsible for writing converted algorithm output to file
    :param Context context: Application context
    :param AbstractStrategy strategy: Chosen strategy for computation
    """

    def __init__(
        self,
        reader: IFileReader,
        parser: IFileInputParser,
        converter: IAlgorithmOutputConverter,
        writer: IFileWriter,
        context: Context,
        strategy: AbstractStrategy,
    ) -> None:
        self._reader = reader
        self._parser = parser
        self._converter = converter
        self._writer = writer
        self._context = context
        self._strategy = strategy

    def run(self) -> None:
        """
        Application launch.

        :return:
        """

        file_contents = self._reader.read(self._context.input_file_path)
        algorithm_input = self._parser.parse(file_contents)
        if is_algorithm_input_valid(algorithm_input, self._context.target_sum):
            algorithm_output = self._strategy.get_pairs(
                algorithm_input, self._context.target_sum
            )
            converted_algorithm_output = self._converter.convert(algorithm_output)
            self._writer.write(
                self._context.output_file_path, converted_algorithm_output
            )
            print(
                f"Application run has been completed successfully. Number of found pairs: {len(algorithm_output)}"
            )


def create_app(context: Context) -> App:
    """
    Application factory.

    :param Context context: Application context
    :return: App instance
    :rtype: App
    """

    read_handlers = FileTypeToReadHandlersMapping[context.input_file_type]
    write_handlers = FileTypeToWriteHandlersMapping[context.output_file_type]
    strategy = StrategyMapping[context.strategy]

    app = App(
        reader=read_handlers.reader(),
        parser=read_handlers.parser(),
        converter=write_handlers.converter(),
        writer=write_handlers.writer(),
        context=context,
        strategy=strategy(),
    )

    return app
