# Project Report

**Status:** In progress.

## Completed Work

| Exercise | Implementation | Tests Passed |
| --- | --- | --- |
| Climbing Stairs | Naive and memoized recursion with call counters | 15 |
| Flat lists | Recursive sum and product | 16 |
| Nested lists | Recursive sum and integer count | 20 |

Each exercise includes base cases, complexity documentation, and automated tests. The list modules also include short explanatory docstrings.

## Key Findings

- **Climbing Stairs:** memoization reduces time from O(2^n) to O(n). At `n = 10`, calls drop from 177 to 19 while both return 89 ways.
- **Flat lists:** sum and product visit each element once, using O(n) time and O(n) stack space.
- **Nested lists:** sum and count visit each element once, using O(n) time and O(n) worst-case stack space. Here n includes integers and sublists across all levels.

The complexity bounds assume constant-cost arithmetic. See [Complexity Analysis](COMPLEXITY_ANALYSIS.md) for base cases, examples, and test links.

## Validation

All **51 tests passed** across the runs recorded on 2026-10-19. Tests cover outputs, counters, cache reuse, empty lists, negative numbers, zeros, nesting, and starting indices. Pytest reported cache-write warnings.

## Remaining Work

Factorial, Fibonacci, bottom-up tabulation, binary search, merge sort, binary tree traversal, and backtracking remain planned. See the [roadmap](ROADMAP.md).
