from algorithm.strategy_mapping import Strategy
from app import App, Context, create_app
from storage.file_type_mapping import FileType


def test_create_app() -> None:
    context = Context(
        input_file_path="input.txt",
        input_file_type=FileType.TXT,
        output_file_path="output.txt",
        output_file_type=FileType.TXT,
        strategy=Strategy.SUBTRACTION,
        target_sum=12,
    )
    app = create_app(context)

    assert isinstance(app, App)
