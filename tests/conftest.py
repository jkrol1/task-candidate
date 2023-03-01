import pytest

from cli import create_cli_parser


@pytest.fixture
def cli_parser():
    return create_cli_parser()


@pytest.fixture
def open_mock_with_set_read_data(mocker):
    def wrapper(file_content):
        mocked_read_data = mocker.mock_open(read_data=file_content)
        mocker.patch("builtins.open", mocked_read_data)

    return wrapper


@pytest.fixture
def open_mock(mocker):
    open_mock = mocker.patch("builtins.open", mocker.mock_open())
    return open_mock


@pytest.fixture
def tmp_txt_file(tmp_path):
    def wrapper(file_content):
        d = tmp_path / "sub"
        d.mkdir()
        p = d / "temp_file.txt"
        p.write_text(file_content)
        return p

    return wrapper
