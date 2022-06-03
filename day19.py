#!/usr/bin/env python
import functools
import hashlib
from re import L


def do_part_a(num_elves):
    def next_round(elves):
        """Go round the circle once, and return the new list of elves"""
        # If there are an odd number of elves, then the last elf will
        # be at the start of the next list
        last_place = [elves[-1]] if len(elves) % 2 else []
        return last_place + elves[0:-1:2]

    elves = list(range(1, num_elves + 1))
    while len(elves) > 1:
        elves = next_round(elves)
    return elves[0]


def do_part_b(num_elves):
    # FIXME This brute force approach is slow!
    elves = list(range(1, num_elves + 1))
    position = 0

    while num_elves > 1:
        index = (position + num_elves // 2) % num_elves
        del elves[index]
        num_elves -= 1
        # Increment position if removed elf is further round the circle
        if index > position:
            position = position + 1
        # loop back to beginning of circle if required
        position = position % num_elves
    return elves[0]


def main():
    num_elves = read_input()

    part_a = do_part_a(num_elves)
    print(f"{part_a=}")

    # part_b = do_part_b(num_elves)
    # print(f"{part_b=}")

    # Look for the pattern
    for x in range(1, 100001):
        if x == do_part_b(x):
            print(x, do_part_b(x))




def read_input() -> int:
    with open("day19.txt") as f:
        return int(f.read().strip())


if __name__ == "__main__":
    main()
