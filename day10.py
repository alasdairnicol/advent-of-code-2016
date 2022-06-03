#!/usr/bin/env python
from typing import Generator


def give(bots, from_bot, low_to, high_to=None):
    low_value, high_value = sorted(bots[from_bot])

    receiver = bots.setdefault(low_to, [])
    receiver.append(low_value)

    receiver = bots.setdefault(high_to, [])
    receiver.append(high_value)

    bots[from_bot] = []


def set_value(bots, bot, value):
    receiver = bots.setdefault(bot, [])
    receiver.append(value)


def parse_instructions(instructions):
    bots = {}
    destinations = {}

    for instruction in instructions:
        words = instruction.split()
        if words[0] == "value":
            bot = f"bot {words[-1]}"
            bots.setdefault(bot, []).append(int(words[1]))

        elif words[0] == "bot":
            from_bot = f"bot {words[1]}"
            destinations[from_bot] = {
                "low_to": f"{words[5]} {words[6]}",
                "high_to": f"{words[10]} {words[11]}",
            }

    return bots, destinations


def main():
    instructions = list(read_input())

    bots, destinations = parse_instructions(instructions)
    while True:
        for bot, values in list(bots.items()):
            if sorted(values) == [17, 61]:
                part_a = int(bot.split()[1])

            if len(values) == 2 and not bot.startswith("output"):
                give(bots, bot, **destinations[bot])
                break  # out of for loop
        else:
            break  # out of while loop

    print(f"{part_a=}")

    part_b = bots["output 0"][0] * bots["output 1"][0] * bots["output 2"][0]
    print(f"{part_b=}")


def read_input() -> Generator[str, None, None]:
    with open("day10.txt") as f:
        return (line.strip() for line in f.readlines())


if __name__ == "__main__":
    main()
