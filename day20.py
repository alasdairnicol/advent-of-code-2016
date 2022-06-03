#!/usr/bin/env python
from typing import Generator


def parse(line):
    return [int(x) for x in line.split("-")]


def do_part_a(lines):
    max_value = -1
    for low, high in lines:
        if low <= max_value + 1 and high > max_value:
            max_value = high

    return max_value + 1


def do_part_b(lines):
    total = 0
    max_value = -1
    for low, high in lines:
        if high <= max_value:
            continue
        if low <= max_value:
            low = max_value + 1
        max_value = max(high, max_value)
        total += high - low + 1
    return (2**32) - total


def main():

    lines = sorted(parse(line) for line in read_input())

    part_a = do_part_a(lines)
    print(f"{part_a=}")

    part_b = do_part_b(lines)
    print(f"{part_b=}")


def read_input() -> Generator[str, None, None]:
    with open("day20.txt") as f:
        return (line.strip() for line in f.readlines())


if __name__ == "__main__":
    main()
