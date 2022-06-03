#!/usr/bin/env python
import itertools
import re
from typing import Generator
from collections import Counter


room_regex = re.compile(
    r"^(?P<name>[a-z-]+)-(?P<sector>\d+)\[(?P<checksum>[a-z]{5})\]$"
)


def shift(letter, number):
    if letter == "-":
        return " "
    x = ord(letter)
    x += number % 26
    if x > 122:
        x -= 26
    return chr(x)


def verify_room(name, checksum):
    counter = Counter(sorted(name.replace("-", "")))
    expected_checksum = "".join(x for (x, y) in counter.most_common(5))
    return checksum == expected_checksum


def main():
    lines = list(read_input())

    rooms = [room_regex.match(room).groups() for room in lines]

    valid_rooms = [room for room in rooms if verify_room(room[0], room[2])]

    part_a = sum(int(room[1]) for room in valid_rooms)
    print(f"{part_a=}")

    for room in valid_rooms:
        name = room[0]
        number = int(room[1])
        decrypted = "".join(shift(l, number) for l in name)

        if "north" in decrypted and "pole" in decrypted:
            part_b = number

    print(f"{part_b=}")


def read_input() -> Generator[str, None, None]:
    with open("day04.txt") as f:
        return (line.strip() for line in f.readlines())


if __name__ == "__main__":
    main()
