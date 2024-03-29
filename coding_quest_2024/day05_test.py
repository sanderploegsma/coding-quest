"""
Coding Quest: 2024/05.
"""

import io

from coding_quest_2024 import day05

EXAMPLE = """\
        base    ta00    cx22    xj84
base       0   55457   63529   61302
ta00   55457       0  111890   35768
cx22   63529  111890       0   98977
xj84   61302   35768   98977       0

Rover 1 route: base -> cx22 -> ta00 -> base -> xj84 -> base
"""


def test_example():
    assert day05.solve(io.StringIO(EXAMPLE)) == 353480
