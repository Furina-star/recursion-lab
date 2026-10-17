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

The project is divided into six phases:

1. **Recursion Fundamentals**: Factorial, Fibonacci, and Climbing Stairs.
2. **Recursion Analysis**: Recursive call counting, recursion trees, and complexity.
3. **Memoization and Dynamic Programming**: Caching, top-down and bottom-up solutions.
4. **Divide and Conquer**: Recursive Binary Search and Merge Sort.
5. **Recursive Data Structures**: Nested lists and binary tree traversal.
6. **Backtracking**: Subsets, permutations, and final comparative analysis.

See [ROADMAP.md](docs/ROADMAP.md) for detailed progress.

## Current Progress

**Climbing Stairs — In Progress**

Implemented:
- Recursive solution with memoization.
- Dictionary-based caching.
- Tracking total calls, cache hits, and cache misses.

Upcoming:
- Naive recursive implementation.
- Performance comparison.
- Edge-case testing.
- Final documentation.

## Getting Started

**Requirements:** Python 3.10+ is recommended.

Run the current exercise from the project root:

```bash
python -m problems.fundamentals.climbing_stairs
```

Optional development setup:

```bash
python -m venv .venv
python -m pip install -r requirements-dev.txt
```

Activate the virtual environment before installing dependencies. To run automated tests once they are implemented:

```bash
python -m pytest
```

## Documentation

- [Learning Roadmap](docs/ROADMAP.md)
- [Complexity Analysis](docs/COMPLEXITY_ANALYSIS.md)

## Project Principles

- Implement algorithms incrementally.
- Prioritize understanding over memorization.
- Compare implementations through measured results.
- Document important discoveries and mistakes.
- Add abstractions or dependencies only when necessary.
