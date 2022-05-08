#!/usr/bin/env python
from typing import Generator
from itertools import permutations


def load_maze(lines):
    grid = set()
    locations = {}
    for y, line in enumerate(lines):
        for x, val in enumerate(line):
            if val == "#":
                continue
            grid.add((x, y))
            try:
                location = int(val)
            except ValueError:
                pass
            else:
                locations[location] = (x, y)

    return grid, locations


def neighbours(point):
    x, y = point
    return [(x, y - 1), (x, y + 1), (x - 1, y), (x + 1, y)]


def find_distances(location, grid, locations):
    starting_point = locations[location]
    distances = {starting_point: 0}
    queue = [starting_point]

    while queue:
        point = queue.pop(0)
        distance = distances[point]
        for neighbour in neighbours(point):
            if neighbour not in grid:
                continue
            elif neighbour in distances:
                continue
            else:
                distances[neighbour] = distance + 1
                queue.append(neighbour)

    return {k: distances.get(v) for k, v in locations.items()}


def calc_path_steps(shortest_paths, perm):
    distance = 0

    for x, y in zip(*((0,) + perm, perm)):
        distance += shortest_paths[x][y]
    return distance


def do_part_a(shortest_paths):
    max_location = max(shortest_paths)

    fewest_steps = None
    for perm in permutations(range(1, max_location + 1)):
        steps = calc_path_steps(shortest_paths, perm)
        fewest_steps = steps if fewest_steps is None else min(fewest_steps, steps)

    return fewest_steps


def do_part_b(shortest_paths):
    max_location = max(shortest_paths)

    fewest_steps = None
    for perm in permutations(range(1, max_location + 1)):
        steps = calc_path_steps(shortest_paths, perm + (0,))
        fewest_steps = steps if fewest_steps is None else min(fewest_steps, steps)

    return fewest_steps


def main():
    lines = list(read_input())
    grid, locations = load_maze(lines)

    shortest_paths = {}
    for location in locations:
        shortest_paths[location] = find_distances(location, grid, locations)

    part_a = do_part_a(shortest_paths)
    print(f"{part_a=}")

    part_b = do_part_b(shortest_paths)
    print(f"{part_b=}")


def read_input() -> Generator[int, None, None]:
    with open("day24.txt") as f:
        return (line.strip() for line in f.readlines())


if __name__ == "__main__":
    main()
