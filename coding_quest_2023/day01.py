"""
Coding Quest: 2023/01.
"""

import sys
from collections import defaultdict
from math import prod
from typing import TextIO


def solve(file: TextIO):
    quantities = defaultdict(lambda: 0)
    for line in file.readlines():
        _, quantity, category = tuple(line.split())
        quantities[category] += int(quantity)

    return prod(q % 100 for q in quantities.values())


def main():
    filename = sys.argv[0].replace(".py", ".txt")

    with open(filename, encoding="utf-8") as file:
        print("Answer:", solve(file))


if __name__ == "__main__":
    main()
