#!/usr/bin/env python


def extend(a):
    b = ("1" if x == "0" else "0" for x in reversed(a))
    return f'{a}0{"".join(b)}'


def expand_to_size(a, size):
    while len(a) < size:
        a = extend(a)
    return a[:size]


def pairs(x):
    """abcdef -> ab, cd, ef"""
    for i in range(0, len(x), 2):
        yield x[i : i + 2]


def checksum(a):
    while len(a) % 2 == 0:
        a = "".join("1" if x == y else "0" for x, y in pairs(a))
    return a


def main():
    initial_state = read_input()

    part_a = checksum(expand_to_size(initial_state, size=272))
    print(f"{part_a=}")

    part_b = checksum(expand_to_size(initial_state, size=35651584))
    print(f"{part_b=}")


def read_input():
    with open("day16.txt") as f:
        return f.read().strip()


if __name__ == "__main__":
    main()
