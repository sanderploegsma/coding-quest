"""
Coding Quest: 2023/01.
"""

import io

from coding_quest_2023 import day01

EXAMPLE = """\
ed669507-8122-4f78-bc59-e1c6518aa3f1 62686 Fuel
707ff3b1-9b0c-4c43-a495-47af7970486f 45574 Food
1d8101bb-ebf1-4802-9da2-27bb4e238313 61915 Mechanical
91034b54-9170-4f7e-97d5-687893171cb5 04859 Water
bf06f8a5-b894-4a06-9b1d-b67236f982da 08414 Water
a056a0fd-0b61-4f38-a874-a464646447af 28211 Frozen
788cc982-73b2-4c73-ae78-c19aef96cfbf 09164 Food
55df7ab8-29fd-463a-a986-98d400437db2 30952 Food
f768ae8a-51f0-48a3-b1db-c7d2ff7b51e5 21834 Mechanical
a3f64ee8-eb55-41bf-9d66-0a4091e7cc2f 46272 Water
"""


def test_example():
    assert day01.solve(io.StringIO(EXAMPLE)) == 187733700
