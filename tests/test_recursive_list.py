from problems.data_structures.recursive_list import recursive_list_sum, recursive_list_product
import pytest


@pytest.mark.parametrize(
    "numbers, expected",
    [
        ([], 0),
        ([5], 5),
        ([4, 7, 2, 9], 22),
        ([0, 0, 0], 0),
        ([-2, -3, -4], -9),
        ([-2, 0, 5], 3),
    ]
)
def test_recursive_list_sum_multiple_inputs(numbers, expected):
    assert recursive_list_sum(numbers) == expected


@pytest.mark.parametrize(
    "numbers, expected",
    [
        ([], 1),
        ([5], 5),
        ([4, 7, 2, 9], 504),
        ([2, 0, 5], 0),
        ([-2, -3, -4], -24),
        ([-2, -3, 4], 24),
    ]
)
def test_recursive_list_product_multiple_inputs(numbers, expected):
    assert recursive_list_product(numbers) == expected


@pytest.mark.parametrize(
    "index, expected_sum, expected_product",
    [
        (1, 18, 126),
        (3, 9, 9),
        (4, 0, 1),
        (5, 0, 1),
    ]
)
def test_recursive_list_starting_index(index, expected_sum, expected_product):
    numbers = [4, 7, 2, 9]

    assert recursive_list_sum(numbers, index) == expected_sum
    assert recursive_list_product(numbers, index) == expected_product
