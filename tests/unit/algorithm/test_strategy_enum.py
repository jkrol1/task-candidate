from algorithm.strategy_mapping import Strategy


def test_strategy_values_to_list():
    strategies = Strategy.values_to_list()

    assert ["sorting", "subtraction"] == strategies
