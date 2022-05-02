#!/usr/bin/env python
from typing import Generator
from dataclasses import dataclass
from itertools import permutations


@dataclass
class Node:
    name: str
    size: int
    used: int
    available: int

    @classmethod
    def from_line(cls, line):
        words = line.split()
        return cls(
            name=words[0],
            size=int(words[1][:-1]),
            used=int(words[2][:-1]),
            available=int(words[3][:-1]),
        )

    @property
    def coordinates(self):
        return tuple(int(n[1:]) for n in self.name.split("-")[1:])

    @property
    def is_large(self):
        return self.used > 100


def viable_pair(node_a, node_b):
    if node_a.used == 0:
        return False
    if node_a.name == node_b.name:
        return False
    if node_a.used > node_b.available:
        return False

    return True


def find_viable_pairs(nodes):
    return [
        (node_a, node_b)
        for node_a, node_b in permutations(nodes, 2)
        if viable_pair(node_a, node_b)
    ]


def main():
    lines = list(read_input())
    nodes = [Node.from_line(line) for line in lines[2:]]

    viable_pairs = find_viable_pairs(nodes)
    part_a = len(viable_pairs)
    print(f"{part_a=}")

    nodes_dict = {node.coordinates: node for node in nodes}

    # Find largest x value (index of right-most column)
    max_x = max(x for x, _ in nodes_dict)

    # Show there is a single empty node
    empty_nodes = [n for n in nodes if n.used == 0]
    assert len(empty_nodes) == 1
    empty_node = empty_nodes[0]
    empty_x, empty_y = empty_node.coordinates

    # Show the only viable moves are to move data to the empty node
    for _, node_b in viable_pairs:
        assert node_b.name == empty_node.name

    # Show all nodes with size >= 100 have used >= 100, therefore the
    # data on these can never be moved.
    LARGE_SIZE = 100
    for node in nodes:
        if node.size >= LARGE_SIZE:
            assert node.used >= LARGE_SIZE

    # All the large rows are in a single row
    large_nodes = [node for node in nodes if node.is_large]
    large_rows = set({n.coordinates[1] for n in large_nodes})
    assert len(large_rows) == 1
    large_row = large_rows.pop()

    # Find the right-most column in the large row where the node isn't large
    column = 0
    for x in range(0, max_x + 1):
        if not nodes_dict[(x, large_row)].size >= LARGE_SIZE:
            column = x

    moves = []

    # To count number of moves, consider the following example, where _ is the empty node,
    # G is the target data, and # are large nodes.
    #
    # .......G
    # ........
    # ........
    # ........
    # ...#####
    # ........
    # ......_.
    #
    # 1. First we'll move the empty node (_) to A so that it's left of all the large nodes
    #
    # .......G
    # ........
    # ........
    # ........
    # ...#####
    # ........
    # .._.....

    moves.append(empty_x - column)

    # 2. Now move the empty node to the top row
    # .._....G
    # ........
    # ........
    # ........
    # ...#####
    # ........
    # ........

    moves.append(empty_y)

    # 3. Now move the empty node to the left of the target data
    #
    # .._....G
    # ........
    # ........
    # ........
    # ...#####
    # ........
    # ........

    moves.append(max_x - 1 - column)

    # 4. Move the empty node and target data to the left
    #
    # _G......
    # ........
    # ........
    # ........
    # ...#####
    # ........
    # ........
    #
    # This takes 5 moves for each column we move G, because the
    # empty node has to move 4 times before can move G again
    #
    # 0    1    2    3    4    5
    # ._G  .G_  .G.  .G.  .G.  _G.
    # ...  ...  .._  ._.  _..  ...
    #

    moves.append(5 * (max_x - 1))

    #
    # 5. Finally swap the empty node and target data
    #
    # G_......
    # ........
    # ........
    # ........
    # ...#####
    # ........
    # ........

    moves.append(1)

    # So the minimum number of moves is the sum of all the steps above
    total_moves = sum(moves)
    part_b = total_moves

    print(f"{part_b=}")


def read_input() -> Generator[int, None, None]:
    with open("day22.txt") as f:
        return (line.strip() for line in f.readlines())


if __name__ == "__main__":
    main()
