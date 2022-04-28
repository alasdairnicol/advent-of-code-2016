#!/usr/bin/env python
import functools
import hashlib
from collections import Counter
from re import L
from typing import Generator


def complete(part_a, part_b):
    return len(part_a) == 8 and "_" not in part_b


@functools.lru_cache(maxsize=None)
def gen_key(salt, num, num_hashes=1):
    digest = f"{salt}{num}"
    for x in range(num_hashes):
        digest = hashlib.md5(digest.encode("utf-8")).hexdigest()
    return digest


def has_triplet(key):
    for i in range(len(key) - 2):
        if len(set(key[i : i + 3])) == 1:
            return key[i]
    return None


def is_valid_key(salt, num, num_hashes):
    key = gen_key(salt, num, num_hashes)
    char = has_triplet(key)
    if not char:
        return False
    else:
        next_1000 = (gen_key(salt, num + i, num_hashes) for i in range(1, 1001))
        expected = char * 5
        if any(expected in k for k in next_1000):
            return key
        return False


def find_index(salt, num_hashes):
    x = 0
    num_keys = 0
    while num_keys < 64:
        x += 1
        if is_valid_key(salt, x, num_hashes):
            num_keys += 1
    return x


def main():
    salt = read_input()

    part_a = find_index(salt, 1)
    print(f"{part_a=}")

    part_b = find_index(salt, 2017)
    print(f"{part_b=}")


def read_input() -> str:
    with open("day14.txt") as f:
        return f.read().strip()


if __name__ == "__main__":
    main()
