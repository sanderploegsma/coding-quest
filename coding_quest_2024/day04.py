import sys
from typing import TextIO

from coding_quest import distance_3d


def parse(line: str):
    columns = line.rsplit(maxsplit=4)
    return float(columns[2]), float(columns[3]), float(columns[4])


def solve(file: TextIO):
    coordinates = list(map(parse, file.readlines()[1:]))
    min_dist = min(
        distance_3d(c1, c2) for c1 in coordinates for c2 in coordinates if c1 != c2
    )
    return round(min_dist, ndigits=3)


def main():
    filename = sys.argv[0].replace(".py", ".txt")

    with open(filename, encoding="utf-8") as file:
        print("Answer:", solve(file))


if __name__ == "__main__":
    main()
