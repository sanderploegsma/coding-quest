import sys
from typing import TextIO

CHARACTERS = ".", "#"


def solve(file: TextIO, width=100):
    c = 0
    result = ""
    for n in file.read().split():
        result += CHARACTERS[c] * int(n)
        c = 1 - c

    formatted = ""
    for i in range(0, len(result), width):
        formatted += result[i: i + width] + "\n"

    return formatted


def main():
    filename = sys.argv[0].replace(".py", ".txt")

    with open(filename, encoding="utf-8") as file:
        print("Answer:", solve(file))


if __name__ == "__main__":
    main()
