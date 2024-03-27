import sys
from collections import defaultdict
from typing import TextIO


def parse_line(line: str):
    name, cost_type, cost = line.split()
    if cost_type in {"Discount", "Rebate"}:
        return name, int(cost) * -1
    return name, int(cost)


def solve(file: TextIO):
    totals = defaultdict(lambda: 0)
    for line in file.readlines():
        name, cost = parse_line(line)
        totals[name] += cost

    return min(totals.values())


def main():
    filename = sys.argv[0].replace(".py", ".txt")

    with open(filename, encoding="utf-8") as file:
        print("Answer:", solve(file))


if __name__ == "__main__":
    main()
