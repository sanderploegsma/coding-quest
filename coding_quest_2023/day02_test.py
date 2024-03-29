"""
Coding Quest: 2023/02.
"""

import io

from coding_quest_2023 import day02

EXAMPLE = """\
30635
34132
46818
15895
37924
52364
31114
4040
6676
53800
"""


def test_example():
    assert day02.solve(io.StringIO(EXAMPLE)) == 17837
