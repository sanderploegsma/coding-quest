import sys
from typing import TextIO

from coding_quest import windowed, distance_3d


def solve(file: TextIO):
    coordinates = list(tuple(map(int, line.split())) for line in file.readlines())
    return sum(
        int(distance_3d(*window)) for window in windowed(coordinates, window_size=2)
    )


def main():
    filename = sys.argv[0].replace(".py", ".txt")

    with open(filename, encoding="utf-8") as file:
        print("Answer:", solve(file))


if __name__ == "__main__":
    main()
