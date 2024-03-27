import sys
from typing import TextIO

WINNING_NUMBERS = (12, 48, 30, 95, 15, 55, 97)


def solve(file: TextIO):
    def score(win_count: int):
        if win_count < 3:
            return 0
        return pow(10, win_count - 3)

    tickets = list(tuple(map(int, line.split())) for line in file.readlines())
    return sum(score(sum(x in WINNING_NUMBERS for x in ticket)) for ticket in tickets)


def main():
    filename = sys.argv[0].replace(".py", ".txt")

    with open(filename, encoding="utf-8") as file:
        print("Answer:", solve(file))


if __name__ == "__main__":
    main()
