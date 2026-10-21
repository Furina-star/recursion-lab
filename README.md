# Recursion Lab

A hands-on Python learning project exploring recursive algorithms, their execution behavior, complexity, and optimization techniques.

## Objectives

- Understand base cases and recursive cases.
- Trace recursive calls and understand the call stack.
- Analyze time and space complexity.
- Identify overlapping subproblems and redundant computations.
- Apply memoization and dynamic programming.
- Explore divide-and-conquer, recursive data structures, and backtracking.

## Project Scope

The project is divided into five phases:

1. **Recursion Fundamentals**: Factorial, Fibonacci, and Climbing Stairs.
2. **Memoization and Dynamic Programming**: Caching, top-down and bottom-up solutions.
3. **Divide and Conquer**: Recursive Binary Search and Merge Sort.
4. **Recursive Data Structures**: Flat lists, nested lists, linked lists, and binary tree traversal.
5. **Backtracking**: Subsets, permutations, and final comparative analysis.

See [ROADMAP.md](docs/ROADMAP.md) for detailed progress.

## Current Progress

**Recursive Lists — Completed**

- [Flat lists](problems/data_structures/recursive_list.py): recursively sum or multiply integers by advancing an index.
- [Nested lists](problems/data_structures/nested_list.py): recursively sum or count integers, including inside sublists.
- [Linked lists](problems/data_structures/linked_list.py): recursively count nodes or sum their values by following `next` links; an empty list is `None`.
- Simple module docstrings explain each operation and its complexity.
- All 60 list tests pass: 16 for flat lists, 20 for nested lists, and 24 for linked lists. Coverage includes empty lists, negative numbers, zeros, nesting, starting positions, node construction, unchanged links and values, and the linked-list demo output.

All six functions take O(n) time and O(n) worst-case stack space. For nested lists, n counts all elements across all levels, including sublists; for linked lists, n counts reachable nodes. Linked-list inputs must be finite and acyclic, and long lists are limited by Python's recursion depth. See [Complexity Analysis](docs/COMPLEXITY_ANALYSIS.md) for the explanations and examples. Binary tree traversal is still planned.

**Climbing Stairs — Completed**

Implemented:
- Recursive solution with memoization.
- Dictionary-based caching.
- Tracking total calls, cache hits, and cache misses.
- Naive recursive implementation.
- Performance comparison.
- Edge-case testing.
- Final documentation.

Naive recursion repeats subproblems and takes O(2^n) time with O(n) stack space. Memoization caches results, reducing time to O(n) with O(n) total auxiliary space. At `n = 10`, both return 89 ways, using 177 calls (naive) versus 19 (memoized). All 15 Climbing Stairs tests pass; see the [measured results](docs/COMPLEXITY_ANALYSIS.md).

## Getting Started

**Requirements:** Python 3.10+ is recommended.

Run the list exercises from the project root:

```bash
python -m problems.data_structures.recursive_list
python -m problems.data_structures.nested_list
python -m problems.data_structures.linked_list
```

The flat-list example prints `22` and `504`; the nested-list example prints `3` and `2`; the linked-list example (`-5 -> 10 -> 2 -> None`) prints `3` nodes and a sum of `7`. Run Climbing Stairs with `python -m problems.fundamentals.climbing_stairs`.

Optional development setup:

```bash
python -m venv .venv
python -m pip install -r requirements-dev.txt
```

Activate the virtual environment before installing dependencies. To run the automated tests:

```bash
python -m pytest
```

To run only the list tests:

```bash
python -m pytest tests/test_recursive_list.py tests/test_nested_list.py tests/test_linked_list.py -q
```

## Documentation

- [Learning Roadmap](docs/ROADMAP.md)
- [Complexity Analysis](docs/COMPLEXITY_ANALYSIS.md)
- [Project Report (in progress)](docs/FINAL_REPORT.md)

## Project Principles

- Implement algorithms incrementally.
- Prioritize understanding over memorization.
- Compare implementations through measured results.
- Document important discoveries and mistakes.
- Add abstractions or dependencies only when necessary.
