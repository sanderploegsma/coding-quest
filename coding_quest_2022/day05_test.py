"""
Coding Quest: 2022/05.
"""

import pytest

from coding_quest_2022 import day05


@pytest.mark.parametrize(
    ("description", "number", "previous_hash", "expected"),
    [
        (
            "Original iPhone still in box",
            3595421,
            "0000000000000000000000000000000000000000000000000000000000000000",
            "00000078f97879b26be6baf2adb520b126f84ed10464ed4e9a77b8ed87e07468",
        ),
        (
            "Apollo 11 moon rock",
            27703084,
            "00000078f97879b26be6baf2adb520b126f84ed10464ed4e9a77b8ed87e07468",
            "00000068a1e823c97e72ff22b0450dc4cfa66495b6ac56266edb0389c2d9a045",
        ),
    ],
)
def test_hash_function(
    description: str, number: int, previous_hash: str, expected: str
):
    assert (
        day05.next_hash(desc=description, num=number, hash_=previous_hash) == expected
    )
