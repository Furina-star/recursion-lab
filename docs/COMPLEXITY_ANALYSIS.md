# Recursion Lab — Complexity Analysis

## Purpose

Document the time complexity, space complexity, and observed execution behavior of recursive algorithms implemented throughout the project.

## 1. Climbing Stairs

### Problem Description

Given a nonnegative integer `n`, count the distinct ordered ways to climb `n` steps using moves of one or two steps.

Both implementations use `ways(0) = ways(1) = 1` and `ways(n) = ways(n - 1) + ways(n - 2)`. Zero steps has one solution: take no moves. Each recursive call reduces `n` until a base case returns; pending calls then add their two results as the stack unwinds.

### Implementations

| Approach | Time Complexity | Auxiliary Space |
|---|---|---|
| Naive Recursion | O(2^n) | O(n) |
| Memoized Recursion | O(n) | O(n) |

- **Naive recursion:** evaluates both branches every time, repeatedly solving overlapping subproblems. Time is exponential: O(2^n) is an upper bound (the tighter bound is Theta(phi^n), where phi is approximately 1.618). The deepest call chain uses O(n) stack space.
- **Memoized recursion:** stores results for `n >= 2` in a dictionary and returns cached results on later visits. With an initially empty cache, each non-base subproblem is computed once, giving O(n) time and O(n) total auxiliary space for the cache and stack.

These bounds use the usual constant-cost arithmetic model. Bottom-up tabulation is planned but not implemented.

### Experiment: Recursive Call Counting

Results verified by [the pytest suite](../tests/test_climbing_stairs.py), with fresh counters and an empty cache for each input:

| Input `n` | Output (both) | Naive calls | Memoized calls | Cache hits | Cache misses |
|---|---|---|---|---|---|
| 0 | 1 | 1 | 1 | 0 | 0 |
| 1 | 1 | 1 | 1 | 0 | 0 |
| 2 | 2 | 3 | 3 | 0 | 1 |
| 3 | 3 | 5 | 5 | 0 | 2 |
| 4 | 5 | 9 | 7 | 1 | 3 |
| 5 | 8 | 15 | 9 | 2 | 4 |
| 10 | 89 | 177 | 19 | 7 | 9 |

Calls include the initial invocation, base cases, and cache hits. Base cases return before cache lookup, so they count as neither hits nor misses. Repeating `n = 5` with the populated cache adds one call and one hit, with no new misses.

Validation: `python -m pytest tests/test_climbing_stairs.py -q` returned **15 passed** on 2026-10-19 (one warning about writing pytest's cache). The tests check outputs, counters, and cache reuse; they do not benchmark runtime.

### Findings

At `n = 10`, memoization reduces calls from 177 to 19 (about 89% fewer) while returning the same 89 ways. For a fresh cache and `n >= 2`, memoized calls grow as `2n - 1`, while naive calls grow as `2 * ways(n) - 1`.

### Conclusion

Memoization removes repeated computation at the cost of O(n) cached entries. Both recursive approaches retain O(n) stack depth; caching does not remove the recursion-depth limit.

---

## 2. Future Algorithms

Complexity analyses for Factorial, Fibonacci, Binary Search, Merge Sort, tree traversal, and backtracking will be added as the project progresses.
