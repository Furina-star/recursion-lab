# Complexity Analysis

## Summary

| Algorithm | Time | Auxiliary Space |
| --- | --- | --- |
| Climbing Stairs: naive | O(2^n) | O(n) stack |
| Climbing Stairs: memoized | O(n) | O(n) cache and stack |
| Flat-list sum and product | O(n) | O(n) stack |
| Nested-list sum and count | O(n) | O(n) worst-case stack |

These bounds assume constant-cost arithmetic and the default starting index. Memoization starts with an empty cache.

## Climbing Stairs

Count the ways to climb n steps using moves of one or two steps.

- **Base cases:** `ways(0) = ways(1) = 1`.
- **Recursive case:** `ways(n) = ways(n - 1) + ways(n - 2)`.
- **Naive:** repeats subproblems, giving an O(2^n) time upper bound.
- **Memoized:** caches each subproblem, reducing time to O(n).
- **Space:** both have O(n) stack depth; memoization also stores O(n) cached results.

At `n = 10`, both return **89 ways**. Naive recursion makes **177 calls**; memoization makes **19 calls**, including **8 cache hits** and **9 misses**. Base cases count as calls but not as cache hits or misses.

## Flat Lists

[recursive_list.py](../problems/data_structures/recursive_list.py) processes one element at a time by advancing an index.

- `recursive_list_sum` adds elements and returns `0` at the end.
- `recursive_list_product` multiplies elements and returns `1` at the end.

For n elements, each function visits every element once: **O(n) time**. Calls wait for the remaining elements, using **O(n) stack space**.

Example: `[4, 7, 2, 9]` has a sum of `22` and a product of `504`.

## Nested Lists

[nested_list.py](../problems/data_structures/nested_list.py) processes each sublist before continuing with the next element.

- `nested_list_sum` adds integers across all levels.
- `count_nested_integers` counts integers across all levels.
- Both return `0` at the end; empty sublists contribute nothing.

Here n counts all elements across all levels, including sublists. Each is visited once: **O(n) time**. Pending calls grow while advancing through lists and entering sublists, using **O(n) worst-case stack space**.

Example: `[[], [1, []], 2]` has a sum of `3` and an integer count of `2`.

## Test Results

Results recorded on 2026-10-19:

| Test File | Passed | Coverage |
| --- | --- | --- |
| [test_climbing_stairs.py](../tests/test_climbing_stairs.py) | 15 | Outputs, call counts, and cache reuse |
| [test_recursive_list.py](../tests/test_recursive_list.py) | 16 | Empty lists, signs, zeros, and starting indices |
| [test_nested_list.py](../tests/test_nested_list.py) | 20 | Empty sublists, nesting, signs, zeros, and starting indices |

All **51 tests passed** across the recorded runs, with pytest cache-write warnings. Tests verify behavior; complexity comes from code analysis, not runtime benchmarks.
