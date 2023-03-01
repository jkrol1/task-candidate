import pytest

from algorithm.strategy_mapping import Strategy
from app import create_app


@pytest.mark.parametrize("file_content", ["10,2,3,4,5,6,7,12,0,4,8,4,8"])
def test_app_with_txt_file_and_subtraction_strategy(tmp_txt_file, context):
    expected_output_file_content = "[(5, 7), (0, 12), (4, 8), (4, 8)]"
    context.input_file_path = context.output_file_path = str(tmp_txt_file)
    app = create_app(context)
    app.run()
    output_file_content = tmp_txt_file.read_text()
    assert expected_output_file_content == output_file_content


@pytest.mark.parametrize("file_content", ["10,2,3,4,5,6,7,12,0,4,8,4,8"])
def test_app_with_txt_file_and_sorting_strategy(tmp_txt_file, context):
    expected_output_file_content = "[(0, 12), (2, 10), (4, 8), (4, 8), (5, 7)]"
    context.input_file_path = context.output_file_path = str(tmp_txt_file)
    context.strategy = Strategy.SORTING
    app = create_app(context)
    app.run()
    output_file_content = tmp_txt_file.read_text()
    assert expected_output_file_content == output_file_content
