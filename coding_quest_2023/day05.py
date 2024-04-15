"""
Coding Quest: 2023/05.
"""

import sys
from typing import TextIO

from coding_quest import display


def solve(file: TextIO, width: int = 50, height: int = 10):
    screen = [[0 for _ in range(width)] for _ in range(height)]
    for line in file.readlines():
        left, top, w, h = tuple(map(int, line.split()))
        for x in range(left, left + w):
            for y in range(top, top + h):
                screen[y][x] = 1 - screen[y][x]

    return display(screen)


def main():
    filename = sys.argv[0].replace(".py", ".txt")

    with open(filename, encoding="utf-8") as file:
        print(solve(file))


if __name__ == "__main__":
    main()
