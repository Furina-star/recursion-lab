"""

"""

def climb_stairs(n: int, cache: dict, stats: dict) -> int:
    stats["calls"] += 1
    if n <= 1:
        return 1

    if n in cache:
        print(f"CACHE HIT: {n}")
        stats["hits"] += 1
        return cache[n]

    print(f"CACHE MISS: {n}")
    stats["misses"] += 1

    cache[n] = climb_stairs(n - 1, cache, stats) + climb_stairs(n - 2, cache, stats)

    return cache[n]

def main():
    cache = {}

    stats = {
        "calls": 0,
        "hits": 0,
        "misses": 0
    }

    s = 7

    print("\n", climb_stairs(s, cache, stats))
    print("\n", cache)
    print("\n", stats)

if __name__ == "__main__":
    main()