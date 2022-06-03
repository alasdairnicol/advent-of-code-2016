#!/usr/bin/env python
from typing import Generator
import math


def parse_discs(lines):
    discs = []
    for i, line in enumerate(lines, 1):
        words = line.rstrip(".").split()
        num_positions = int(words[3])
        initial_position = int(words[-1])
        remainder = (
            num_positions - ((initial_position + i) % num_positions)
        ) % num_positions
        discs.append((num_positions, remainder))
    return discs


def find_starting_time(discs):
    t = 0
    step = 1
    for num_positions, remainder in discs:
        while t % num_positions != remainder:
            t += step
        step = (step * num_positions) // math.gcd(
            step, num_positions
        )  # use math.lcm in Python 3.9+
    return t


def main():
    lines = list(read_input())
    # Disc for part b
    lines.append("Disc #7 has 11 positions; at time=0, it is at position 0.")

    discs = parse_discs(lines)

    # Exclude final disc, it's only for part b
    part_a = find_starting_time(discs[:-1])
    print(f"{part_a=}")

    part_b = find_starting_time(discs)
    print(f"{part_b=}")


def read_input() -> Generator[str, None, None]:
    with open("day15.txt") as f:
        return (line.strip() for line in f.readlines())


if __name__ == "__main__":
    main()
