import io

from coding_quest_2024 import day04

EXAMPLE = """\
System                                  Dist         X         Y         Z
Proxima Centauri                       4.247     2.945    -3.056    -0.143
Barnard's star                         5.963     4.958     2.980     1.449
Luhman 16 A                            6.503     1.697    -6.249     0.600
WISE J085510.83-071442.5               7.532    -3.967    -5.664     2.985
Wolf 359                               7.856    -1.916    -3.938     6.522
"""


def test_example():
    assert day04.solve(io.StringIO(EXAMPLE)) == 3.508
