#!/usr/bin/env python
from dataclasses import dataclass
import itertools
from math import floor
from typing import Generator


@dataclass(frozen=True)
class FloorLayout:
    elevator: int
    floor_1: frozenset
    floor_2: frozenset
    floor_3: frozenset
    floor_4: frozenset

    @property
    def floors(self):
        return {
            1: self.floor_1,
            2: self.floor_2,
            3: self.floor_3,
            4: self.floor_4,
        }

    def next_elevator_floors(self):
        if self.elevator > 1:
            yield self.elevator - 1
        if self.elevator < 4:
            yield self.elevator + 1

    def new_layout_after_move(self, new_floor, elevator_items_set):
        return FloorLayout(
            new_floor,
            floor_1=self.floor_1 - elevator_items_set
            if self.elevator == 1
            else self.floor_1 | elevator_items_set
            if new_floor == 1
            else self.floor_1,
            floor_2=self.floor_2 - elevator_items_set
            if self.elevator == 2
            else self.floor_2 | elevator_items_set
            if new_floor == 2
            else self.floor_2,
            floor_3=self.floor_3 - elevator_items_set
            if self.elevator == 3
            else self.floor_3 | elevator_items_set
            if new_floor == 3
            else self.floor_3,
            floor_4=self.floor_4 - elevator_items_set
            if self.elevator == 4
            else self.floor_4 | elevator_items_set
            if new_floor == 4
            else self.floor_4,
        )

    def target(self):
        return FloorLayout(
            4,
            floor_1=frozenset(),
            floor_2=frozenset(),
            floor_3=frozenset(),
            floor_4=self.floor_1 | self.floor_2 | self.floor_3,
        )


def possible_moves(floor_layout: FloorLayout):
    current_floor_items = floor_layout.floors[floor_layout.elevator]
    for elevator_items in itertools.chain(
        itertools.combinations(current_floor_items, 1),
        itertools.combinations(current_floor_items, 2),
    ):
        elevator_items_set = frozenset(elevator_items)
        left_behind = current_floor_items - elevator_items_set
        if is_floor_valid(left_behind):
            for new_floor in floor_layout.next_elevator_floors():
                new_floor_items = floor_layout.floors[new_floor] | elevator_items_set
                if is_floor_valid(new_floor_items):
                    yield floor_layout.new_layout_after_move(
                        new_floor, elevator_items_set
                    )


def is_floor_valid(floor):
    microchips = {x[:-1] for x in floor if x[-1] == "M"}
    generators = {x[:-1] for x in floor if x[-1] == "G"}
    unpaired_microchips = {m for m in microchips if m not in generators}
    return not (unpaired_microchips and generators)


def description_to_code(description):
    prefix = description[:2].upper()
    suffix = "G" if "generator" in description else "M"
    return f"{prefix}{suffix}"


def parse_line(line):
    if "nothing relevant" in line:
        return frozenset()

    line = line.rstrip(".")

    contents = frozenset(description_to_code(desc) for desc in line.split(" a ")[1:])
    return contents


def main():
    lines = list(read_input())

    layout_a = FloorLayout(1, *(parse_line(line) for line in lines))

    part_a = minimum_number_of_steps(layout_a)
    print(f"{part_a=}")

    layout_b = FloorLayout(
        1,
        floor_1=layout_a.floor_1 | frozenset(["ELG", "ELM", "DIG", "DIM"]),
        floor_2=layout_a.floor_2,
        floor_3=layout_a.floor_3,
        floor_4=layout_a.floor_4,
    )

    part_b = minimum_number_of_steps(layout_b)
    print(f"{part_b=}")


def minimum_number_of_steps(layout):
    seen_layouts = {layout: 0}
    queue = [layout]

    target = layout.target()

    while target not in seen_layouts:
        layout = queue.pop(0)
        num_moves = seen_layouts[layout]
        for new_layout in possible_moves(layout):
            if new_layout in seen_layouts:
                continue
            else:
                seen_layouts[new_layout] = num_moves + 1
                queue.append(new_layout)

    return seen_layouts[target]


def read_input() -> Generator[str, None, None]:
    with open("day11.txt") as f:
        return (line.strip() for line in f.readlines())


if __name__ == "__main__":
    main()
