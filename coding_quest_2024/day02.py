import sys
from typing import TextIO

INTERNAL_SYSTEMS = 192, 168
PASSENGER_WIFI = 10, 0


def solve(file: TextIO):
    internal_systems, passenger_wifi = 0, 0

    for packet in list(bytes.fromhex(line) for line in file.readlines()):
        length = int.from_bytes(packet[2:4])
        src_ip = packet[12], packet[13]
        dst_ip = packet[16], packet[17]
        if src_ip == INTERNAL_SYSTEMS or dst_ip == INTERNAL_SYSTEMS:
            internal_systems += length
        if src_ip == PASSENGER_WIFI or dst_ip == PASSENGER_WIFI:
            passenger_wifi += length

    return f"{internal_systems}/{passenger_wifi}"


def main():
    filename = sys.argv[0].replace(".py", ".txt")

    with open(filename, encoding="utf-8") as file:
        print("Answer:", solve(file))


if __name__ == "__main__":
    main()
