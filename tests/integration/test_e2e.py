from pathlib import Path
from typing import Callable

import pytest
from _pytest.capture import CaptureFixture

from algorithm.strategy_mapping import Strategy
from main import main

INITIAL_FILE_CONTENT = "10,2,3,4,5,6,7,12,0,4,8,4,8"
STRATEGY_EXPECTED_OUTPUT_FILE_CONTENT = [
    (Strategy.SUBTRACTION_DICT.value, "[(2, 10), (5, 7), (0, 12), (4, 8), (4, 8)]"),
    (Strategy.SORTING.value, "[(0, 12), (2, 10), (4, 8), (4, 8), (5, 7)]"),
]


@pytest.mark.parametrize(
    "strategy, expected_output_file_content", STRATEGY_EXPECTED_OUTPUT_FILE_CONTENT
)
def test_main_with_txt_file(
    tmp_txt_file: Callable[[str], Path],
    strategy: str,
    expected_output_file_content: str,
    capsys: CaptureFixture[str],
) -> None:
    file = tmp_txt_file(INITIAL_FILE_CONTENT)
    file_path = str(file)
    main(["-i", file_path, "-o", file_path, "-s", strategy])
    output_file_content = file.read_text()
    captured_out = capsys.readouterr().out
    expected_captured_out = (
        "Application run has been completed successfully. Number of found pairs: 5\n"
    )

    assert expected_output_file_content == output_file_content
    assert expected_captured_out == captured_out
