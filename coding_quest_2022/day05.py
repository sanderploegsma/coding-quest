"""
Coding Quest: 2022/05.
"""

import sys
from hashlib import sha256
from typing import TextIO


def parse(line: str):
    fields = line.strip().split("|")
    return fields[0], int(fields[1]), fields[3]


def next_hash(desc: str, num: int, hash_: str):
    hasher = sha256()
    hasher.update(f"{desc}|{num}|{hash_}".encode())
    return hasher.hexdigest()


def solve(file: TextIO):
    current_hash = "0" * 64
    for desc, num, hash_ in map(parse, file.readlines()):
        if next_hash(desc, num, current_hash) == hash_:
            print("Record valid:", desc)
            current_hash = hash_
        else:
            print("Record invalid:", desc)
            hash_ = ""
            num = 0
            while not hash_.startswith("0" * 6):
                num += 1
                hash_ = next_hash(desc, num, current_hash)
            current_hash = hash_

    return current_hash


def main():
    filename = sys.argv[0].replace(".py", ".txt")

    with open(filename, encoding="utf-8") as file:
        print("Answer:", solve(file))


if __name__ == "__main__":
    main()
