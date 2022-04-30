#!/usr/bin/env python
from typing import Generator


def cpy(registers, location, x, y):
    registers[y] = registers.get(x, x)
    return location + 1


def inc(registers, location, x):
    registers[x] += 1
    return location + 1


def dec(registers, location, x):
    registers[x] -= 1
    return location + 1


def jnz(registers, location, x, y):
    if registers.get(x, x) != 0:
        location += y
    else:
        location += 1
    return location


def parse_line(line):
    words = line.split()
    if words[0] == "cpy":
        func = cpy
    elif words[0] == "inc":
        func = inc
    elif words[0] == "dec":
        func = dec
    elif words[0] == "jnz":
        func = jnz
    args = [x if x in "abcd" else int(x) for x in words[1:]]
    return func, *args


def main():
    lines = list(read_input())
    instructions = [parse_line(line) for line in lines]

    part_a = run_program(instructions, c=0)
    print(f"{part_a=}")
    part_b = run_program(instructions, c=1)
    print(f"{part_b=}")


def run_program(instructions, c=0):

    registers = {
        "a": 0,
        "b": 0,
        "c": c,
        "d": 0,
    }

    location = 0

    while location < len(instructions):
        func, *args = instructions[location]
        location = func(registers, location, *args)

    return registers["a"]


def read_input() -> Generator[int, None, None]:
    with open("day12.txt") as f:
        return (line.strip() for line in f.readlines())


if __name__ == "__main__":
    main()
