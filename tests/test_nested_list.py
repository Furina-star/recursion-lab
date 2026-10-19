from problems.data_structures.nested_list import nested_list_sum, count_nested_integers
import pytest


@pytest.mark.parametrize(
    "numbers, expected",
    [
        ([], 0),
        ([[], [[]]], 0),
        ([5], 5),
        ([1, 2, 3], 6),
        ([1, [2, [3]], 4], 10),
        ([[], [1, []], 2], 3),
        ([[-2, 0], [5, [-3]]], 0),
        ([[[[7]]]], 7),
    ]
)
def test_nested_list_sum_multiple_inputs(numbers, expected):
    assert nested_list_sum(numbers) == expected


@pytest.mark.parametrize(
    "numbers, expected",
    [
        ([], 0),
        ([[], [[]]], 0),
        ([5], 1),
        ([1, 2, 3], 3),
        ([1, [2, [3]], 4], 4),
        ([[], [1, []], 2], 2),
        ([[-2, 0], [5, [-3]]], 4),
        ([[[[7]]]], 1),
    ]
)
def test_count_nested_integers_multiple_inputs(numbers, expected):
    assert count_nested_integers(numbers) == expected


@pytest.mark.parametrize(
    "index, expected_sum, expected_count",
    [
        (1, 9, 3),
        (2, 4, 1),
        (3, 0, 0),
        (4, 0, 0),
    ]
)
def test_nested_list_starting_index(index, expected_sum, expected_count):
    numbers = [1, [2, [3]], 4]

    assert nested_list_sum(numbers, index) == expected_sum
    assert count_nested_integers(numbers, index) == expected_count
