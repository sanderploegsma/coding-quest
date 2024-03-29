"""
Coding Quest: 2023/02.
"""

import sys
from statistics import mean
from typing import TextIO


def solve(file: TextIO):
    values = list(map(int, file.readlines()))

    valid = []
    for value in values:
        value_bits = f"{value:016b}"
        if len(value_bits.replace("0", "")) % 2 == 0:
            valid.append(int(value_bits[1:], 2))

    return round(mean(valid))


def main():
    filename = sys.argv[0].replace(".py", ".txt")

    with open(filename, encoding="utf-8") as file:
        print("Answer:", solve(file))


if __name__ == "__main__":
    main()
