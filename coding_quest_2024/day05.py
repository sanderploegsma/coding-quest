"""
Coding Quest: 2024/05.
"""

import sys
from typing import TextIO


def parse_distances(table: str):
    rows = list(line.split() for line in table.splitlines()[1:])
    distances: dict[tuple[str, str], int] = {}
    for row in rows:
        src = row[0]
        for col_num, col in enumerate(row[1:]):
            dst = rows[col_num][0]
            distances[src, dst] = int(col)
    return distances


def parse_route(line: str):
    _, route = tuple(line.split(": "))
    return route.split(" -> ")


def solve(file: TextIO):
    contents = file.read().split("\n\n")
    distances = parse_distances(contents[0])
    routes = list(map(parse_route, contents[1].splitlines()))

    total = 0
    for route in routes:
        for i in range(len(route) - 1):
            total += distances[route[i], route[i + 1]]

    return total


def main():
    filename = sys.argv[0].replace(".py", ".txt")

    with open(filename, encoding="utf-8") as file:
        print("Answer:", solve(file))


if __name__ == "__main__":
    main()
