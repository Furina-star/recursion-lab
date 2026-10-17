"""
Climbing Stairs

Given an integer n, count the distinct ways to climb a staircase
with n steps when each move can climb either 1 or 2 steps. The order of moves
matters.

Example:
    n = 4 -> 5 ways: (1, 1, 1, 1), (1, 1, 2), (1, 2, 1), (2, 1, 1), (2, 2).

Recurrence:
    ways(0) = ways(1) = 1
    ways(n) = ways(n - 1) + ways(n - 2) for n >= 2

This module compares naive recursion with memoized recursion and tracks
recursive calls, cache hits, and cache misses. Naive recursion takes O(2^n)
time and O(n) stack space; memoization takes O(n) time and O(n) total space.
"""

# Naive Recursion
def climb_stairs_naive(n: int, naive_stats: dict) -> int:
    naive_stats["calls"] += 1
    if n <= 1:
        return 1

    return climb_stairs_naive(n - 1, naive_stats) + climb_stairs_naive(n - 2, naive_stats)

# Memorized Recursion
def climb_stairs_memoized(n: int, cache: dict, mem_stats: dict) -> int:
    mem_stats["calls"] += 1
    if n <= 1:
        return 1

    if n in cache:
        print(f"CACHE HIT: {n}")
        mem_stats["hits"] += 1
        return cache[n]

    print(f"CACHE MISS: {n}")
    mem_stats["misses"] += 1

    cache[n] = climb_stairs_memoized(n - 1, cache, mem_stats) + climb_stairs_memoized(n - 2, cache, mem_stats)

    return cache[n]

# Main
def main():
    cache = {}

    naive_stats = {
        "calls": 0
    }
    mem_stats = {
        "calls": 0,
        "hits": 0,
        "misses": 0
    }

    s = 20

    naive = climb_stairs_naive(s, naive_stats)
    memorized = climb_stairs_memoized(s, cache, mem_stats)

    print("\nNaive Recursion:", naive)
    print(naive_stats)
    print("\nMemorized Recursion:", memorized)
    print(mem_stats)

if __name__ == "__main__":
    main()
