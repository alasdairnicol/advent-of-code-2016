#!/usr/bin/env python
from typing import Generator


class Computer:
    instructions = None
    location = None
    registers = None
    output = None
    states = None

    def __init__(self, instructions, a=0, b=0, c=0, d=0):
        self.location = 0
        self.instructions = list(instructions)
        self.output = []
        self.registers = {
            "a": a,
            "b": b,
            "c": c,
            "d": d,
        }

    @property
    def state(self):
        return (self.location, tuple(self.registers.items()))

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

    def out(self, x):
        self.output.append(self.registers.get(x, x))
        self.location += 1

    def do_instruction(self):
        func_name, *args = self.instructions[self.location]
        func = getattr(self, func_name)
        func(*args)


def parse_line(line):
    words = line.split()
    func = words[0]
    args = [x if x in "abcd" else int(x) for x in words[1:]]
    return [func] + args


def check_output(output):
    return set(output[0::2]) == {0} and set(output[1::2]) == {1}


def main():
    lines = list(read_input())
    instructions = [parse_line(line) for line in lines]

    i = 1
    while True:
        computer = Computer(instructions, a=i)
        out = run_program(computer)
        if check_output(out):
            part_a = i
            break
        i += 1

    print(f"{part_a=}")


def run_program(computer):
    seen_states = set()
    while computer.state not in seen_states:
        seen_states.add(computer.state)
        computer.do_instruction()

    return computer.output


def read_input() -> Generator[int, None, None]:
    with open("day25.txt") as f:
        return (line.strip() for line in f.readlines())


if __name__ == "__main__":
    main()
