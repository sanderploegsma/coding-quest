#!/usr/bin/env python

import os
import argparse

from jinja2 import Environment

SCRIPT_DIR = os.path.join(os.path.dirname(__file__))
TEMPLATE_DIR = os.path.join(SCRIPT_DIR, "templates")
ROOT_DIR = os.path.join(SCRIPT_DIR, "..")


def generate(year: int, day: int):
    output_dir = os.path.join(ROOT_DIR, f"coding_quest_{year}")
    day_padded = f"{day:02}"
    env = Environment(autoescape=False, optimized=False)

    def generate_file(template_name: str, output_name: str):
        with open(
            os.path.join(TEMPLATE_DIR, template_name), "r", encoding="utf-8"
        ) as f:
            template = env.from_string(f.read())

        with open(os.path.join(output_dir, output_name), "x", encoding="utf-8") as f:
            template.stream(year=year, day=day_padded).dump(f)

    generate_file("input.txt.j2", f"day{day_padded}.txt")
    generate_file("solution.py.j2", f"day{day_padded}.py")
    generate_file("test.py.j2", f"day{day_padded}_test.py")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("year", type=int)
    parser.add_argument("day", type=int)
    args = parser.parse_args()
    generate(**vars(args))


if __name__ == "__main__":
    main()
