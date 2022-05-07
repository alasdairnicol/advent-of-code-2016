#!/usr/bin/env python
from hashlib import md5

GRID_SIZE = 4
STARTING_POSITION = (0, 0)
VAULT = (GRID_SIZE - 1, GRID_SIZE - 1)


def doors(passcode):
    """
    Returns a list of bools representing
    whether the [up, down, left, right]
    doors are open
    """
    digest = md5(passcode.encode()).hexdigest()
    open_chars = "bcdef"
    return [x in open_chars for x in digest[:4]]


def get_possible_moves(passcode, position):
    x, y = position
    u, d, l, r = doors(passcode)
    if u and y > 0:
        yield passcode + "U", (x, y - 1),
    if d and y < GRID_SIZE - 1:
        yield passcode + "D", (x, y + 1),
    if l and x > 0:
        yield passcode + "L", (x - 1, y)
    if r and x < GRID_SIZE - 1:
        yield passcode + "R", (x + 1, y),


def main():
    initial_passcode = read_input()
    position = STARTING_POSITION

    queue = {(initial_passcode, position)}

    possible_routes = set()

    while queue:
        passcode, position = queue.pop()
        for new_passcode, new_position in get_possible_moves(passcode, position):
            if new_position == VAULT:
                possible_routes.add(new_passcode)
            else:
                queue.add((new_passcode, new_position))

    sorted_routes = sorted(possible_routes, key=lambda x: len(x))
    part_a = sorted_routes[0][len(initial_passcode) :]
    print(f"{part_a=}")
    part_b = len(sorted_routes[-1][len(initial_passcode) :])
    print(f"{part_b=}")


def read_input():
    with open("day17.txt") as f:
        return f.read().strip()


if __name__ == "__main__":
    main()
