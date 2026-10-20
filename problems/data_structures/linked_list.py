class Node:
    def __init__(self, value: int, next_node=None):
        self.value = value
        self.next = next_node

def count_nodes(node: Node) -> int:
    if node is None:
        return 0

    return count_nodes(node.next) + 1

def main():
    head = Node(4)
    head.next = Node(7)
    head.next.next = Node(8)

    result = count_nodes(head)

    print(result)

if __name__ == "__main__":
    main()