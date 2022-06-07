#!/usr/bin/env python
from collections import deque


def next_round_a(elves):
    """Go round the circle once, and return the new list of elves"""
    # If there are an odd number of elves, then the last elf will
    # be at the start of the next list
    last_place = [elves[-1]] if len(elves) % 2 else []
    return last_place + elves[0:-1:2]


def highest_power_of_two(x):
    a = 1
    while x > 1:
        a <<= 1
        x >>= 1
    return a


def do_part_a(num_elves):
    """
    Solve using solution to the Josephus Problem
    """
    # Find remainder where num_elves = 2**a + remainder
    a = highest_power_of_two(num_elves)
    remainder = num_elves - a
    return 2 * remainder + 1


def do_part_a_alternative(num_elves):
    """
    Solve using solution to the Josephus trick

    Move most significant bit to end

    e.g.   41 = 101001
     solution =  010011 = 19
    """
    return int(f"{bin(num_elves)[3:]}1", 2)


def do_part_b_two_deques(num_elves):
    elves = range(1, num_elves + 1)
    left = deque(elves[0 : num_elves // 2])
    right = deque(elves[num_elves // 2 :])
    while left:
        # remove elf:
        right.popleft()
        # rotate elf that just played
        right.append(left.popleft())
        # rebalance every other turn
        if len(right) - len(left) == 2:
            left.append(right.popleft())
    return right[0]


def calc_part_b(num_elves):
    power_of_three = 1
    while 3 * power_of_three <= num_elves:
        power_of_three *= 3

    diff = num_elves - power_of_three

    if diff == 0:
        return num_elves
    elif diff <= power_of_three:
        return diff
    else:
        return 2 * num_elves - 3 * power_of_three


def main():
    num_elves = read_input()

    part_a = do_part_a(num_elves)
    print(f"{part_a=}")

    part_b = do_part_b_two_deques(num_elves)
    print(f"{part_b=}")


def read_input() -> int:
    with open("day19.txt") as f:
        return int(f.read().strip())


if __name__ == "__main__":
    main()
