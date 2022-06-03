#!/usr/bin/env python
import itertools
from typing import Generator


def swap_position(password, x, y):
    password[x], password[y] = password[y], password[x]


def swap_letter(password, a, b):
    x = password.index(a)
    y = password.index(b)
    swap_position(password, x, y)


def reverse_positions(password, x, y):
    password[x : y + 1] = reversed(password[x : y + 1])


def rotate_left(password, x):
    x = (x + len(password)) % len(password)
    password.extend(password[:x])
    password[:x] = []


def rotate_right(password, x):
    rotate_left(password, len(password) - x)


def rotate_based_on(password, a):
    num = password.index(a)
    if num >= 4:
        num += 1
    num += 1
    rotate_right(password, num)


def move_to(password, x, y):
    char = password[x]
    del password[x]
    password.insert(y, char)


def scramble_password(lines, password_in):
    password = list(password_in)
    for line in lines:
        words = line.split()
        if words[0:2] == ["swap", "position"]:
            swap_position(password, int(words[2]), int(words[5]))
        elif words[0:2] == ["swap", "letter"]:
            swap_letter(password, words[2], words[5])
        elif words[0:2] == ["rotate", "left"]:
            rotate_left(password, int(words[2]))
        elif words[0:2] == ["rotate", "right"]:
            rotate_right(password, int(words[2]))
        elif words[0:2] == ["rotate", "based"]:
            rotate_based_on(password, words[6])
        elif words[0] == "reverse":
            reverse_positions(password, int(words[2]), int(words[4]))
        elif words[0] == "move":
            move_to(password, int(words[2]), int(words[5]))
        # print("".join(password))
    return "".join(password)


def unscramble_password(lines, target):
    # There are only 8!=40320 possible passwords, so it was easier
    # to try scrambling them all rather than writing an unscramble function
    for password in itertools.permutations("abcdefgh"):
        if scramble_password(lines, password) == target:
            return "".join(password)


def main():
    lines = list(read_input())

    part_a = scramble_password(lines, "abcdefgh")
    print(f"{part_a=}")

    part_b = unscramble_password(lines, "fbgdceah")
    print(f"{part_b=}")


def read_input() -> Generator[str, None, None]:
    with open("day21.txt") as f:
        return (line.strip() for line in f.readlines())


if __name__ == "__main__":
    main()
