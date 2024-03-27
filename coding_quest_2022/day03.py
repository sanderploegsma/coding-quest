import sys
from typing import TextIO
import math

from coding_quest import windowed, squared


def solve(file: TextIO):
    def distance(a: tuple[int, int, int], b: tuple[int, int, int]):
        return int(
            math.sqrt(
                squared(b[0] - a[0]) + squared(b[1] - a[1]) + squared(b[2] - a[2])
            )
        )

    coordinates = list(tuple(map(int, line.split())) for line in file.readlines())
    return sum(distance(*window) for window in windowed(coordinates, window_size=2))


def main():
    filename = sys.argv[0].replace(".py", ".txt")

    with open(filename, encoding="utf-8") as file:
        print("Answer:", solve(file))


if __name__ == "__main__":
    main()
