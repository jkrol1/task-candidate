import pytest

from algorithm.strategy_mapping import Strategy
from app import Context, create_app
from cli import create_cli_parser
from storage.file_type_mapping import FileType


@pytest.fixture
def cli_parser():
    return create_cli_parser()


@pytest.fixture
def parse_cli_args_with_system_exit_handling(cli_parser):
    def wrapper(args):
        try:
            args = cli_parser.parse_args(args)
        except SystemExit:
            pass
        return args

    return wrapper


@pytest.fixture
def context():
    return Context(
        input_file_path="input.txt",
        input_file_type=FileType.TXT,
        output_file_path="output.txt",
        output_file_type=FileType.TXT,
        strategy=Strategy.SUBTRACTION,
        target_sum=12,
    )


@pytest.fixture
def app(context):
    app = create_app(context)
    return app


@pytest.fixture
def open_mock(mocker):
    def wrapper(file_contents: str):
        mocked_read_data = mocker.mock_open(read_data=file_contents)
        mocker.patch("builtins.open", mocked_read_data)

    return wrapper


@pytest.fixture
def write_mock(mocker):
    write_mock = mocker.patch("builtins.open", mocker.mock_open())
    write_mock.write = mocker.stub()
    return write_mock


@pytest.fixture
def tmp_txt_file(tmp_path, file_content):
    d = tmp_path / "sub"
    d.mkdir()
    p = d / "temp_file.txt"
    p.write_text(file_content)
    return p
