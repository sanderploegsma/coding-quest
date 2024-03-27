import io

from coding_quest_2024 import day03

EXAMPLE = "12 6 4 1 9 5 5 1 9 1 7"
EXPECTED = """\
..........
..######..
..#.......
..#####...
..#.......
..#.......
"""


def test_example():
    assert day03.solve(io.StringIO(EXAMPLE), width=10) == EXPECTED
