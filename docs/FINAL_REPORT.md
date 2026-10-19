# Recursion Lab — Project Report

Status: In progress; this report currently covers the completed Climbing Stairs exercise.

## Climbing Stairs

Both approaches count ordered sequences of one-step and two-step moves using `ways(n) = ways(n - 1) + ways(n - 2)`, with `ways(0) = ways(1) = 1`.

- **Naive recursion:** explores both branches and repeats subproblems; O(2^n) time and O(n) stack space.
- **Memoized recursion:** caches each non-base result for reuse; O(n) time with an empty cache and O(n) total auxiliary space, including the stack.

The pytest suite passed all 15 tests on 2026-10-19, checking outputs and counters for `n = 0, 1, 2, 3, 4, 5, 10`, plus cache reuse. At `n = 5`, both return 8 ways, with 15 naive calls versus 9 memoized calls. At `n = 10`, both return 89 ways, with 177 versus 19 calls (about 89% fewer). Reusing the cache for `n = 5` adds only one call and one hit.

These call counts demonstrate reduced repeated work; runtime was not benchmarked. Both approaches still use a linear-depth call stack. See [Complexity Analysis](COMPLEXITY_ANALYSIS.md) for the full results and counter definitions.

Remaining project work, including bottom-up tabulation and other algorithms, is tracked in the [roadmap](ROADMAP.md).
