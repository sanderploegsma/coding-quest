import sys
from statistics import mean
from typing import TextIO

from coding_quest import windowed

WINDOW_SIZE = 60


def solve(file: TextIO):
    count = 0
    samples = list(int(value) for value in file.readlines())
    for window in windowed(samples, window_size=60):
        avg = mean(window)
        if avg < 1500 or avg > 1600:
            count += 1
    return count


def main():
    filename = sys.argv[0].replace(".py", ".txt")

    with open(filename, encoding="utf-8") as file:
        print("Answer:", solve(file))


if __name__ == "__main__":
    main()
