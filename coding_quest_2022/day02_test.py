import io

from coding_quest_2022 import day02

EXAMPLE = """\
46 46 5 87 92 73
95 73 30 12 97 27
34 49 42 41 58 16
33 5 91 60 40 88
74 52 63 74 19 31
13 31 13 6 68 4
57 36 41 17 40 15
29 59 20 85 73 42
31 67 82 51 44 80
48 41 55 12 15 30
"""


def test_example():
    assert day02.solve(io.StringIO(EXAMPLE)) == 110
