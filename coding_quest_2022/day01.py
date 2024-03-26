import sys
from statistics import mean
from typing import TextIO

WINDOW_SIZE = 60


def solve(file: TextIO):
    count = 0
    samples = list(int(value) for value in file.readlines())
    for i in range(len(samples) - WINDOW_SIZE + 1):
        avg = mean(samples[i : i + WINDOW_SIZE])
        if avg < 1500 or avg > 1600:
            count += 1
    return count


def main():
    filename = sys.argv[0].replace(".py", ".txt")

    with open(filename, encoding="utf-8") as file:
        print("Answer:", solve(file))


if __name__ == "__main__":
    main()
