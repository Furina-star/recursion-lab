"""
Count ways to climb n steps using moves of 1 or 2 steps.
Base cases: ways(0) = ways(1) = 1.
Recurrence: ways(n) = ways(n - 1) + ways(n - 2).
Naive: O(2^n) time and O(n) stack space.
Memoized: O(n) time and O(n) space for the cache and stack.
"""

# Naive Recursion
def climb_stairs_naive(n: int, naive_stats: dict) -> int:
    naive_stats["calls"] += 1
    if n <= 1:
        return 1

    return climb_stairs_naive(n - 1, naive_stats) + climb_stairs_naive(n - 2, naive_stats)

# Memoized Recursion
def climb_stairs_memoized(n: int, cache: dict, mem_stats: dict) -> int:
    mem_stats["calls"] += 1
    if n <= 1:
        return 1

    if n in cache:
        mem_stats["hits"] += 1
        return cache[n]

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

    s = 5

    naive = climb_stairs_naive(s, naive_stats)
    memoized = climb_stairs_memoized(s, cache, mem_stats)

    print("\nNaive Recursion:", naive)
    print(naive_stats)
    print("\nMemoized Recursion:", memoized)
    print(mem_stats)

if __name__ == "__main__":
    main()
