"""
Coding Quest: 2023/04.
"""

import io

from coding_quest_2023 import day04

EXAMPLE = """\
55550000005800f754686973206973206120746573742e205468697320697320
55550000005801f06120746573742e205468616e6b796f752e20202020202020
"""


def test_example():
    assert (
        day04.solve(io.StringIO(EXAMPLE)) == "This is a test. This is a test. Thankyou."
    )
