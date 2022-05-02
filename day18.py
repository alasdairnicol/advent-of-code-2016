#!/usr/bin/env python
import itertools


def is_trap(a, b, c):
    """
    a new tile is a trap only in one of the following situations:
    * Its left and center tiles are traps, but its right tile is not.
    * Its center and right tiles are traps, but its left tile is not.
    * Only its left tile is a trap.
    * Only its right tile is a trap.
    """
    return (
        (a and b and not c)
        or (not a and b and c)
        or (a and not (b or c))
        or (not (a or b) and c)
    )


def safe_count(line):
    return len([x for x in line if not x])


def triples(line):
    a, b, c = itertools.tee(line, 3)
    next(b)
    next(c)
    next(c)
    return zip(*(a, b, c))


def next_line(line):
    padded_line = [False] + line + [False]
    return [is_trap(*triple) for triple in triples(padded_line)]


def print_line(line):
    print("".join("^" if x else "." for x in line))


def num_safe_tiles(line, num_lines):
    safe = safe_count(line)

    for x in range(1, num_lines):
        line = next_line(line)
        safe += safe_count(line)

    return safe


def main():
    line_string = read_input()
    line = [x == "^" for x in line_string]

    part_a = num_safe_tiles(list(line), 40)
    print(f"{part_a=}")

    part_b = num_safe_tiles(list(line), 400000)
    print(f"{part_b=}")


def read_input() -> str:
    with open("day18.txt") as f:
        return f.read().strip()


if __name__ == "__main__":
    main()
