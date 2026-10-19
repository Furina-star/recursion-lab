"""
Sum a list recursively by advancing an index; return 0 at the end.
For n elements: O(n) time and O(n) stack space.
"""


def recursive_list_sum(numbers: list[int], index: int = 0) -> int:
    if len(numbers) <= index:
        return 0

    return numbers[index] + recursive_list_sum(numbers, index + 1)

def main():
    numbers = [4, 7, 2, 9]

    result = recursive_list_sum(numbers)
    print(result)

if __name__ == "__main__":
    main()
