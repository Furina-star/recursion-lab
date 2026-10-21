import pytest

from problems.data_structures.linked_list import Node, count_nodes, main, sum_nodes


def build_list(values):
    head = None
    for value in reversed(values):
        head = Node(value, head)
    return head


@pytest.mark.parametrize(
    "values, expected",
    [
        ([], 0),
        ([5], 1),
        ([0], 1),
        ([-5], 1),
        ([-5, 10, 2], 3),
        ([0, 0, 0], 3),
        ([-2, -3, -4], 3),
        ([4, 4, 4], 3),
    ],
)
def test_count_nodes(values, expected):
    assert count_nodes(build_list(values)) == expected


@pytest.mark.parametrize(
    "values, expected",
    [
        ([], 0),
        ([5], 5),
        ([0], 0),
        ([-5], -5),
        ([-5, 10, 2], 7),
        ([0, 0, 0], 0),
        ([-2, -3, -4], -9),
        ([4, 4, 4], 12),
    ],
)
def test_sum_nodes(values, expected):
    assert sum_nodes(build_list(values)) == expected


def test_node_defaults_to_no_successor():
    node = Node(5)

    assert node.value == 5
    assert node.next is None


def test_node_keeps_supplied_successor():
    tail = Node(2)
    head = Node(10, tail)

    assert head.value == 10
    assert head.next is tail


@pytest.mark.parametrize(
    "offset, expected_count, expected_sum",
    [(1, 2, 12), (2, 1, 2), (3, 0, 0)],
)
def test_traversal_from_successor(offset, expected_count, expected_sum):
    node = build_list([-5, 10, 2])
    for _ in range(offset):
        node = node.next

    assert count_nodes(node) == expected_count
    assert sum_nodes(node) == expected_sum


@pytest.mark.parametrize("operation", [count_nodes, sum_nodes])
def test_traversal_preserves_values_and_links(operation):
    tail = Node(2)
    middle = Node(10, tail)
    head = Node(-5, middle)

    operation(head)

    assert (head.value, middle.value, tail.value) == (-5, 10, 2)
    assert head.next is middle
    assert middle.next is tail
    assert tail.next is None


def test_main_prints_count_and_sum(capsys):
    main()

    assert capsys.readouterr().out == "3\n7\n"
