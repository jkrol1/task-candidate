from argparse import ArgumentParser
from pathlib import Path
from typing import Callable
from unittest.mock import MagicMock

import pytest
from pytest_mock import MockFixture

from cli import create_cli_parser


@pytest.fixture
def cli_parser() -> ArgumentParser:
    return create_cli_parser()


@pytest.fixture
def open_mock_with_set_read_data(mocker: MockFixture) -> Callable[[str], None]:
    def wrapper(file_content: str) -> None:
        mocked_read_data = mocker.mock_open(read_data=file_content)
        mocker.patch("builtins.open", mocked_read_data)

    return wrapper


@pytest.fixture
def open_mock(mocker: MockFixture) -> MagicMock:
    open_mock = mocker.patch("builtins.open", mocker.mock_open())
    return open_mock


@pytest.fixture
def tmp_txt_file(tmp_path: Path) -> Callable[[str], Path]:
    def wrapper(file_content: str) -> Path:
        d = tmp_path / "sub"
        d.mkdir()
        p = d / "temp_file.txt"
        p.write_text(file_content)
        return p

    return wrapper
