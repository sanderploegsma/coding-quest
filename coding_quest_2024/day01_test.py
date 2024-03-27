import io

from coding_quest_2024 import day01

EXAMPLE = """\
AAA: Seat 9997
BBB: Discount 2886
DDD: Luggage 3500
AAA: Tax 156
CCC: Fee 9468
BBB: Fee 9378
AAA: Discount 3103
DDD: Rebate 967
"""


def test_example():
    assert day01.solve(io.StringIO(EXAMPLE)) == 2533
