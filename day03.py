#!/usr/bin/env python
import itertools
from typing import Generator, List


def is_valid_triangle(triangle):
    t1, t2, t3 = sorted(triangle)
    return t1 + t2 > t3


def main():
    lines = list(read_input())
    part_a = do_part_a(lines)
    print(f"{part_a=}")

    part_b = do_part_b(lines)
    print(f"{part_b=}")


def do_part_a(lines):
    triangles = lines
    valid_triangles = [
        triangle for triangle in triangles if is_valid_triangle(triangle)
    ]
    return len(valid_triangles)


def do_part_b(lines):
    transposed = list(itertools.chain.from_iterable(zip(*lines)))
    triangles = [transposed[x : x + 3] for x in range(0, len(transposed), 3)]
    valid_triangles = [
        triangle for triangle in triangles if is_valid_triangle(triangle)
    ]
    return len(valid_triangles)


def read_input() -> Generator[List[int], None, None]:
    with open("day03.txt") as f:
        return ([int(x) for x in line.split()] for line in f.readlines())


if __name__ == "__main__":
    main()
