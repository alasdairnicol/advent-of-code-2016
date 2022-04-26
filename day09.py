#!/usr/bin/env python
from typing import Generator


def main():
    input_string = list(read_input())

    part_a = do_part_a(input_string)
    print(f"{part_a=}")

    print(f"part_b:")


def do_part_a(input_string):
    input_string = iter(input_string)

    output_string = ""
    while True:
        try:
            x = next(input_string)
        except StopIteration:
            break

        if x == "(":
            marker = ""
            while True:
                y = next(input_string)
                if y == ")":
                    break
                marker += y

            length, repeat = (int(x) for x in marker.split("x"))

            letters = "".join(next(input_string) for x in range(length))
            output_string += letters * repeat
        else:
            output_string += x

    return len(output_string)


def read_input() -> Generator[int, None, None]:
    with open("day09.txt") as f:
        return f.read().replace(" ", "").replace("\n", "")


if __name__ == "__main__":
    main()
