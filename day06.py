#!/usr/bin/env python
from typing import Tuple
from collections import Counter


def main():
    columns = read_input()

    counters = (Counter(column) for column in columns)
    most_common = [counter.most_common() for counter in counters]

    part_a = "".join(x[0][0] for x in most_common)
    part_b = "".join(x[-1][0] for x in most_common)

    print(f"{part_a=}")
    print(f"{part_b=}")


def read_input() -> zip[Tuple[str, ...]]:
    with open("day06.txt") as f:
        return zip(*(line.strip() for line in f.readlines()))


if __name__ == "__main__":
    main()
