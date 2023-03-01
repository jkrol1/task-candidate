import pytest

from algorithm.strategy_mapping import Strategy
from main import main


@pytest.mark.parametrize("file_content", ["10,2,3,4,5,6,7,12,0,4,8,4,8"])
def test_main_with_txt_file_and_subtraction_strategy(tmp_txt_file, context):
    expected_output_file_content = "[(5, 7), (0, 12), (4, 8), (4, 8)]"
    tmp_file_path = str(tmp_txt_file)
    main(["-i", tmp_file_path, "-o", tmp_file_path])
    output_file_content = tmp_txt_file.read_text()
    assert expected_output_file_content == output_file_content


@pytest.mark.parametrize("file_content", ["10,2,3,4,5,6,7,12,0,4,8,4,8"])
def test_app_with_txt_file_and_sorting_strategy(tmp_txt_file, context):
    expected_output_file_content = "[(0, 12), (2, 10), (4, 8), (4, 8), (5, 7)]"
    tmp_file_path = str(tmp_txt_file)
    main(["-i", tmp_file_path, "-o", tmp_file_path, "-s", Strategy.SORTING.value])
    output_file_content = tmp_txt_file.read_text()
    assert expected_output_file_content == output_file_content
