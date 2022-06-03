#!/usr/bin/env python
from typing import Generator


class Computer:
    instructions = None
    location = None
    registers = None

    def __init__(self, instructions, a=0, b=0, c=0, d=0):
        self.location = 0
        self.instructions = list(instructions)
        self.registers = {
            "a": a,
            "b": b,
            "c": c,
            "d": d,
        }

    def cpy(self, x, y):
        self.registers[y] = self.registers.get(x, x)
        self.location += 1

    def inc(self, x):
        self.registers[x] += 1
        self.location += 1

    def dec(self, x):
        self.registers[x] -= 1
        self.location += 1

    def jnz(self, x, y):
        if self.registers.get(x, x) != 0:
            self.location += self.registers.get(y, y)
        else:
            self.location += 1

    def add(self, x, y):
        self.registers[y] += self.registers[x]
        self.location += 1

    def mul(self, x, y):
        self.registers[y] *= self.registers.get(x, x)
        self.location += 1

    def tgl(self, x):
        tgl_location = self.location + self.registers.get(x, x)
        try:
            func_name, *args = self.instructions[tgl_location]
        except IndexError:
            pass
        else:
            if len(args) == 1:
                if func_name == "inc":
                    new_func_name = "dec"
                else:
                    new_func_name = "inc"
            else:
                if func_name == "jnz":
                    new_func_name = "cpy"
                else:
                    new_func_name = "jnz"
            self.instructions[tgl_location][0] = new_func_name
        self.location += 1

    def do_instruction(self):
        func_name, *args = self.instructions[self.location]
        func = getattr(self, func_name)
        try:
            func(*args)
        except TypeError:
            self.location += 1


def parse_line(line):
    words = line.split()
    func = words[0]
    args = [x if x in "abcd" else int(x) for x in words[1:]]
    return [func] + args


def main():
    lines = list(read_input())

    # Replace instructions with mult to avoid nested loops
    lines[5:10] = [
        "mul d c",
        "add c a",
        "cpy 0 c",
        "cpy 0 d",
        "jnz 0 0",  # no-op
    ]

    instructions = [parse_line(line) for line in lines]
    computer = Computer(instructions, a=7)
    part_a = run_program(computer)
    print(f"{part_a=}")

    instructions = [parse_line(line) for line in lines]
    computer = Computer(instructions, a=12)
    part_b = run_program(computer)
    print(f"{part_b=}")


def run_program(computer):
    while computer.location < len(computer.instructions):
        computer.do_instruction()

    return computer.registers["a"]


def read_input() -> Generator[str, None, None]:
    with open("day23.txt") as f:
        return (line.strip() for line in f.readlines())


if __name__ == "__main__":
    main()
