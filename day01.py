#!/usr/bin/env python
from typing import Generator


def turn_left(direction):
    x, y = direction
    return (-y, x)


def turn_right(direction):
    x, y = direction
    return (y, -x)


def main():
    instructions = list(read_input())

    part_a = do_part_a(instructions)
    print(f"{part_a=}")
    part_b = do_part_b(instructions)
    print(f"{part_b=}")


def do_part_a(instructions):
    direction = (0, 1)
    position = (0, 0)

    for instruction in read_input():
        turn = instruction[0]
        blocks = int(instruction[1:])
        if turn == "L":
            direction = turn_left(direction)
        elif turn == "R":
            direction = turn_right(direction)
        else:
            raise ValueError(f"Invalid turn {turn}")

        position = (
            position[0] + int(blocks) * direction[0],
            position[1] + int(blocks) * direction[1],
        )

    return abs(position[0]) + abs(position[1])


def do_part_b(instructions):
    visited = set()
    direction = (0, 1)
    position = (0, 0)

    for instruction in read_input():
        turn = instruction[0]
        blocks = int(instruction[1:])
        if turn == "L":
            direction = turn_left(direction)
        elif turn == "R":
            direction = turn_right(direction)
        else:
            raise ValueError(f"Invalid turn {turn}")

        for step in range(1, blocks + 1):
            position = (
                position[0] + direction[0],
                position[1] + direction[1],
            )
            if position in visited:
                return abs(position[0]) + abs(position[1])

            visited.add(position)


def read_input() -> Generator[str, None, None]:
    with open("day01.txt") as f:
        return (x.strip() for x in f.read().split(","))


if __name__ == "__main__":
    main()
