package com.github.sanderploegsma.codingquest

import kotlin.test.Test
import kotlin.test.assertEquals

class Year2022Day03Test {
    private val example = """
0 0 0
-2 -3 14
5 13 -15
8 -6 5
0 0 0
""".trim().lines()

    @Test
    fun testAnswer() {
        assertEquals(85, Year2022Day03.solve(example))
    }
}
