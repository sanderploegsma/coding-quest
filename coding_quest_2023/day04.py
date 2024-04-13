"""
Coding Quest: 2023/04.
"""

import sys
from typing import TextIO


def solve(file: TextIO):
    parts = {}

    for packet in list(bytes.fromhex(line) for line in file.readlines()):
        if packet[0:2] != b"UU":
            continue

        seq_nr = packet[6]
        checksum = packet[7]
        payload = packet[8:]

        if sum(payload) % 256 == checksum:
            parts[seq_nr] = payload.decode("utf-8")

    return "".join(part for _, part in sorted(parts.items())).strip()


def main():
    filename = sys.argv[0].replace(".py", ".txt")

    with open(filename, encoding="utf-8") as file:
        print("Answer:", solve(file))


if __name__ == "__main__":
    main()
