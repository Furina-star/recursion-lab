"""
Sum a nested list recursively; return 0 at the end.
Count integers in a nested list recursively; return 0 at the end.
For n total elements (including sublists): both use O(n) time and O(n) stack space.
"""

# Sum all the elements inside a nested list
def nested_list_sum(numbers: list, index: int = 0) -> int:
    if index >= len(numbers):
        return 0

    current = numbers[index]

    if isinstance(current, list):
        sub_list = nested_list_sum(current)
        return sub_list + nested_list_sum(numbers, index + 1)

    return numbers[index] + nested_list_sum(numbers, index + 1)

# Count the length of nested list
def count_nested_integers(numbers: list, index: int = 0) -> int:
    if index >= len(numbers):
        return 0

    current = numbers[index]

    if isinstance(current, list):
        sub_list = count_nested_integers(current)
        return sub_list + count_nested_integers(numbers, index + 1)

    return 1 + count_nested_integers(numbers, index + 1)

def main():
    numbers = [[], [1, []], 2]

    result1 = nested_list_sum(numbers)
    result2 = count_nested_integers(numbers)

    print(result1)
    print(result2)

if __name__ == "__main__":
    main()