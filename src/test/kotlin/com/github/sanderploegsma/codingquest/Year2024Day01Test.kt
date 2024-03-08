package com.github.sanderploegsma.codingquest

import kotlin.test.Test
import kotlin.test.assertEquals

class Year2024Day01Test {
    private val example = """
AAA: Seat 9997
BBB: Discount 2886
DDD: Luggage 3500
AAA: Tax 156
CCC: Fee 9468
BBB: Fee 9378
AAA: Discount 3103
DDD: Rebate 967
""".trim().lines()

    @Test
    fun testAnswer() {
        assertEquals(2533, Year2024Day01.solve(example))
    }
}
