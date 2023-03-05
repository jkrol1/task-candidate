from algorithm.strategies import AbstractStrategy


def test_create_pair_from_values():
    assert AbstractStrategy.create_pair_from_values(10, 5) == (5, 10)
    assert AbstractStrategy.create_pair_from_values(5, 10) == (5, 10)
