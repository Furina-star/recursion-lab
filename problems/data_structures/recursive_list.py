"""
Sum a list recursively by advancing an index; return 0 at the end.
Product a list recursively by advancing an index; return 1 at the end.
For n elements: O(n) time and O(n) stack space.
"""

# Sum of all element in a list
def recursive_list_sum(numbers: list[int], index: int = 0) -> int:
    if len(numbers) <= index:
        return 0

    return numbers[index] + recursive_list_sum(numbers, index + 1)

# Product of all element in a list
def recursive_list_product(numbers: list[int], index: int = 0) -> int:
    if len(numbers) <= index:
        return 1

    return numbers[index] * recursive_list_product(numbers, index + 1)

def main():
    numbers = [4, 7, 2, 9]

    result1 = recursive_list_sum(numbers)
    result2 = recursive_list_product(numbers)
    print(result1)
    print(result2)

if __name__ == "__main__":
    main()
