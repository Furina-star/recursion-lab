# Recursion Lab — Complexity Analysis

## Purpose

Document the time complexity, space complexity, and observed execution behavior of recursive algorithms implemented throughout the project.

## 1. Climbing Stairs

### Problem Description

Given `n` steps, determine the number of distinct ways to reach the top when each move can climb either one or two steps.

### Implementations

| Approach | Time Complexity | Auxiliary Space |
|---|---|---|
| Naive Recursion | O(2^n) | O(n) |
| Memoized Recursion | O(n) | O(n) |
| Bottom-Up Dynamic Programming | O(n) | O(1) |

The bounds above assume nonnegative inputs. The naive time bound is an exponential upper bound. The memoized implementation uses both a cache and a recursive call stack.

### Experiment: Recursive Call Counting

Input: `n = 7`

Expected output: `21`

| Metric | Naive | Memoized |
|---|---|---|
| Total calls | To be measured | 13 expected |
| Cache hits | N/A | 4 expected |
| Cache misses | N/A | 6 expected |
| Output | 21 expected | 21 expected |

These expected values will be checked against the completed implementations.

### Findings

Pending completion of comparative experiments.

### Conclusion

Pending.

---

## 2. Future Algorithms

Complexity analyses for Factorial, Fibonacci, Binary Search, Merge Sort, tree traversal, and backtracking will be added as the project progresses.