import io

from coding_quest_2022 import day03

EXAMPLE = """\
0 0 0
-2 -3 14
5 13 -15
8 -6 5
0 0 0
"""


def test_example():
    assert day03.solve(io.StringIO(EXAMPLE)) == 85
