from algorithm.strategy_mapping import Strategy


def test_strategy_values_to_list() -> None:
    strategies = Strategy.values_to_list()

    assert ["sorting", "subtraction_dict"] == strategies
