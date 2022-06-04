#!/usr/bin/env python


def next_round_a(elves):
    """Go round the circle once, and return the new list of elves"""
    # If there are an odd number of elves, then the last elf will
    # be at the start of the next list
    last_place = [elves[-1]] if len(elves) % 2 else []
    return last_place + elves[0:-1:2]


def do_part_a(num_elves):
    elves = list(range(1, num_elves + 1))
    while len(elves) > 1:
        elves = next_round_a(elves)
    return elves[0]


def brute_force_part_b(num_elves):
    """Warning: This brute force approach is slow!"""
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


def do_part_b(num_elves):
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

    part_b = do_part_b(num_elves)
    print(f"{part_b=}")


def read_input() -> int:
    with open("day19.txt") as f:
        return int(f.read().strip())


if __name__ == "__main__":
    main()
