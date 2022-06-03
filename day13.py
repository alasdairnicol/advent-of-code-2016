#!/usr/bin/env python


def neighbours(point):
    """Returns a generator with the neighbours for a point"""
    x, y = point
    if x >= 1:
        yield (x - 1, y)
    if y >= 1:
        yield (x, y - 1)
    yield (x + 1, y)
    yield (x, y + 1)


def is_open(point, favourite_number):
    x, y = point
    val = x * x + 3 * x + 2 * x * y + y + y * y
    val += favourite_number
    bin_rep = bin(val)
    return bin_rep.count("1") % 2 == 0


def print_maze(favourite_number):
    for y in range(7):
        print(
            "".join(
                "." if is_open((x, y), favourite_number) else "#" for x in range(10)
            )
        )


def main():
    favourite_number = read_input()

    starting_point = (1, 1)
    distances = {starting_point: 0}
    destination = (31, 39)

    queue = [(starting_point)]
    while destination not in distances:
        point = queue.pop(0)
        new_distance = distances[point] + 1
        for neighbour in neighbours(point):
            if neighbour in distances:
                continue
            if is_open(neighbour, favourite_number):
                distances[neighbour] = new_distance
                queue.append(neighbour)
            else:
                distances[neighbour] = None

    part_a = distances[destination]
    print(f"{part_a=}")

    part_b = len([x for x in distances.values() if x is not None and x <= 50])
    print(f"{part_b=}")


def read_input() -> int:
    with open("day13.txt") as f:
        return int(f.read())


if __name__ == "__main__":
    main()
