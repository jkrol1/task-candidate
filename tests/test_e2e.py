import pytest

from algorithm.strategy_mapping import Strategy
from main import main

FILE_CONTENT = "10,2,3,4,5,6,7,12,0,4,8,4,8"
STRATEGY_EXPECTED_OUTPUT = [
    (Strategy.SUBTRACTION.value, "[(5, 7), (0, 12), (4, 8), (4, 8)]"),
    (Strategy.SORTING.value, "[(0, 12), (2, 10), (4, 8), (4, 8), (5, 7)]")
]


@pytest.mark.parametrize("strategy, expected_output_file_content", STRATEGY_EXPECTED_OUTPUT)
@pytest.mark.parametrize("file_content", [FILE_CONTENT])
def test_main_with_txt_file(tmp_txt_file, strategy, expected_output_file_content, context):
    tmp_file_path = str(tmp_txt_file)
    main(["-i", tmp_file_path, "-o", tmp_file_path, "-s", strategy])
    output_file_content = tmp_txt_file.read_text()

    assert expected_output_file_content == output_file_content
