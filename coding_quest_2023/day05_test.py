"""
Coding Quest: 2023/05.
"""

import io

from coding_quest_2023 import day05

EXAMPLE = """\
1 1 6 4
2 2 5 2
1 5 1 3
2 7 5 1
"""

EXPECTED = """\
........
.######.
.#......
.#......
.######.
.#......
.#......
.######.
"""


def test_example():
    assert day05.solve(io.StringIO(EXAMPLE), width=8, height=8) == EXPECTED
