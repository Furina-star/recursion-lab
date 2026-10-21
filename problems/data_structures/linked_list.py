"""Recursively count and sum nodes in a finite, acyclic linked list.

Both operations return 0 for an empty list (None), follow each node's next
link, and leave the list unchanged. For n nodes, each uses O(n) time and
O(n) call-stack space, assuming constant-cost arithmetic. Long lists are
limited by Python's recursion depth; cycles are not detected.
"""


class Node:
    def __init__(self, value: int, next_node=None):
        self.value = value
        self.next = next_node

# Count the total length of all nodes
def count_nodes(node: Node) -> int:
    if node is None:
        return 0

    return count_nodes(node.next) + 1

# Calculate the total sum of all nodes
def sum_nodes(node: Node) -> int:
    if node is None:
        return 0

    return sum_nodes(node.next) + node.value

def main():
    head = Node(-5)
    head.next = Node(10)
    head.next.next = Node(2)

    result1 = count_nodes(head)
    result2 = sum_nodes(head)

    print(result1)
    print(result2)

if __name__ == "__main__":
    main()
