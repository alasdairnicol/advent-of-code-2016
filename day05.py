#!/usr/bin/env python
import itertools
import hashlib
from typing import Generator


def complete(part_a, part_b):
    return len(part_a) == 8 and "_" not in part_b


def main():
    door_id = read_input()

    x = 0

    part_a = []
    part_b = ["_"] * 8

    while True:
        trial = f"{door_id}{x}".encode("utf-8")
        digest = hashlib.md5(trial).hexdigest()
        if digest.startswith("00000"):
            # Update
            if len(part_a) < 8:
                part_a.append(digest[5])
            try:
                if part_b[int(digest[5])] == "_":
                    part_b[int(digest[5])] = digest[6]
            except (IndexError, ValueError):
                pass
            if complete(part_a, part_b):
                break

        x += 1

    part_a = "".join(part_a)
    part_b = "".join(part_b)

    print(f"{part_a=}")
    print(f"{part_b=}")


def read_input() -> str:
    with open("day05.txt") as f:
        return f.read().strip()


if __name__ == "__main__":
    main()
