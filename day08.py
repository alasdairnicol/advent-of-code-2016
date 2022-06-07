#!/usr/bin/env python
from typing import Generator

WIDTH = 50
HEIGHT = 6

letters_dict = {
    frozenset(
        [(0, 1), (0, 2), (0, 3), (0, 4), (1, 0), (1, 5), (2, 0), (2, 5), (3, 1), (3, 4)]
    ): "C",
    frozenset(
        [
            (0, 0),
            (0, 1),
            (0, 2),
            (0, 3),
            (0, 4),
            (0, 5),
            (1, 0),
            (1, 2),
            (1, 5),
            (2, 0),
            (2, 2),
            (2, 5),
            (3, 0),
            (3, 5),
        ]
    ): "E",
    frozenset(
        [
            (0, 0),
            (0, 1),
            (0, 2),
            (0, 3),
            (0, 4),
            (0, 5),
            (1, 0),
            (1, 2),
            (2, 0),
            (2, 2),
            (3, 0),
        ]
    ): "F",
    frozenset(
        [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (1, 5), (2, 5), (3, 5)]
    ): "L",
    frozenset(
        [
            (0, 1),
            (0, 2),
            (0, 3),
            (0, 4),
            (1, 0),
            (1, 5),
            (2, 0),
            (2, 5),
            (3, 1),
            (3, 2),
            (3, 3),
            (3, 4),
        ]
    ): "O",
    frozenset(
        [
            (0, 1),
            (0, 2),
            (0, 5),
            (1, 0),
            (1, 3),
            (1, 5),
            (2, 0),
            (2, 3),
            (2, 5),
            (3, 0),
            (3, 4),
        ]
    ): "S",
    frozenset(
        [(0, 0), (0, 1), (1, 2), (2, 3), (2, 4), (2, 5), (3, 2), (4, 0), (4, 1)]
    ): "Y",
}


def next_grid(grid, instruction):
    words = instruction.split()
    if words[0] == "rect":
        x, y = [int(n) for n in words[1].split("x")]
        rect = {(i, j) for i in range(x) for j in range(y)}
        return rect | grid

    # rotations
    if words[1] == "row":
        row = int(words[2].split("=")[1])
        amount = int(words[4])
        points = {(x, y) for (x, y) in grid if y == row}
        rotated = {((x + amount) % WIDTH, y) for x, y in points}
        return (grid - points) | rotated

    if words[1] == "column":
        col = int(words[2].split("=")[1])
        amount = int(words[4])
        points = {(x, y) for (x, y) in grid if x == col}
        rotated = {(x, (y + amount) % HEIGHT) for x, y in points}
        return (grid - points) | rotated


def draw_grid(grid):
    for y in range(HEIGHT):
        print("".join("#" if (x, y) in grid else " " for x in range(WIDTH)))
    print()


def split_grid(grid):
    return [
        frozenset(
            [(i, y) for i in range(0, 5) for y in range(HEIGHT) if (x + i, y) in grid]
        )
        for x in range(0, WIDTH, 5)
    ]


def main():
    instructions = read_input()

    grid = set()
    for instruction in instructions:
        grid = next_grid(grid, instruction)

    part_a = len(grid)
    print(f"{part_a=}")
    part_b = "".join(letters_dict.get(points, "?") for points in split_grid(grid))
    print(f"{part_b=}")


def read_input() -> Generator[str, None, None]:
    with open("day08.txt") as f:
        return (line.strip() for line in f.readlines())


if __name__ == "__main__":
    main()
