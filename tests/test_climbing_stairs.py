from problems.fundamentals.climbing_stairs import climb_stairs_naive, climb_stairs_memoized
import pytest

@pytest.mark.parametrize(
    "n, expected, calls",
    [
        (0, 1, 1),
        (1, 1, 1),
        (2, 2, 3),
        (3, 3, 5),
        (4, 5, 9),
        (5, 8, 15),
        (10, 89, 177)

    ]
)

# Test naive
def test_naive_multiple_inputs(n, expected, calls):
    naive_stats = {"calls": 0}

    naive = climb_stairs_naive(n, naive_stats)

    assert naive ==  expected
    assert naive_stats["calls"] == calls

@pytest.mark.parametrize(
    "n, expected, calls, hits, misses",
    [
        (0, 1, 1, 0, 0),
        (1, 1, 1, 0, 0),
        (2, 2, 3, 0, 1),
        (3, 3, 5, 0, 2),
        (4, 5, 7, 1, 3),
        (5, 8, 9, 2, 4),
        (10, 89, 19, 7, 9)

    ]
)

# Test memoized
def test_memoized_multiple_steps(n, expected, calls, hits, misses):
    cache = {}
    memoized_stats = {"calls": 0, "hits": 0,"misses": 0}

    memoized = climb_stairs_memoized(n, cache, memoized_stats)

    assert memoized == expected
    assert memoized_stats["calls"] == calls
    assert memoized_stats["hits"] == hits
    assert memoized_stats["misses"] == misses

# Test cache reuse
def test_memoized_cache_reuse():
    cache = {}
    memoized_stats = {"calls": 0, "hits": 0, "misses": 0}

    first_result = climb_stairs_memoized(5, cache, memoized_stats)
    snapshot = memoized_stats.copy()

    second_result = climb_stairs_memoized(5, cache, memoized_stats)

    assert first_result == second_result == 8
    assert memoized_stats["calls"] == snapshot["calls"] + 1
    assert memoized_stats["hits"] == snapshot["hits"] + 1
    assert memoized_stats["misses"] == snapshot["misses"]