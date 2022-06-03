#!/usr/bin/env python
from typing import Generator

WIDTH = 50
HEIGHT = 6


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


def main():
    instructions = read_input()

    grid = set()
    for instruction in instructions:
        grid = next_grid(grid, instruction)

    part_a = len(grid)
    print(f"{part_a=}")

    print("part_b:")
    draw_grid(grid)


def read_input() -> Generator[str, None, None]:
    with open("day08.txt") as f:
        return (line.strip() for line in f.readlines())


if __name__ == "__main__":
    main()
