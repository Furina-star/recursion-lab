# Project Report

**Status:** In progress.

## Completed Work

| Exercise | Implementation | Tests Passed |
| --- | --- | --- |
| Climbing Stairs | Naive and memoized recursion with call counters | 15 |
| Flat lists | Recursive sum and product | 16 |
| Nested lists | Recursive sum and integer count | 20 |
| Linked lists | Recursive node count and value sum | 24 |

Each exercise includes base cases, complexity documentation, and automated tests. The list modules also include short explanatory docstrings.

## Key Findings

- **Climbing Stairs:** memoization reduces time from O(2^n) to O(n). At `n = 10`, calls drop from 177 to 19 while both return 89 ways.
- **Flat lists:** sum and product visit each element once, using O(n) time and O(n) stack space.
- **Nested lists:** sum and count visit each element once, using O(n) time and O(n) worst-case stack space. Here n includes integers and sublists across all levels.
- **Linked lists:** `count_nodes` and `sum_nodes` follow `next` links until `None`, which returns `0`. Each visits all n reachable nodes once, using O(n) time and O(n) stack space without changing values or links. The example `-5 -> 10 -> 2 -> None` returns a count of `3` and a sum of `7`. Passing an interior node processes the remaining suffix. Inputs must be finite and acyclic; long lists can exceed Python's recursion limit.

The complexity bounds assume constant-cost arithmetic. See [Complexity Analysis](COMPLEXITY_ANALYSIS.md) for base cases, examples, and test links.

## Validation

All **75 tests passed** in the full-suite run on 2026-10-21 using `python -m pytest -q` with Python 3.14.7. Tests cover outputs, counters, cache reuse, empty lists, negative numbers, zeros, nesting, and starting indices. The 24 [linked-list tests](../tests/test_linked_list.py) also cover single-node lists, repeated values, node construction, suffix traversal, preservation of values and links, and demo output. Pytest reported one cache-write warning; no tests failed.

## Remaining Work

Factorial, Fibonacci, bottom-up tabulation, binary search, merge sort, binary tree traversal, and backtracking remain planned. See the [roadmap](ROADMAP.md).
