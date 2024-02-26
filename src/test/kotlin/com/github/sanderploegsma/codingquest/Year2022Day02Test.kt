package com.github.sanderploegsma.codingquest

import kotlin.test.Test
import kotlin.test.assertEquals

class Year2022Day02Test {
    private val winningNumbers = "12 48 30 95 15 55 97"

    private val tickets = """
46 46 5 87 92 73
95 73 30 12 97 27
34 49 42 41 58 16
33 5 91 60 40 88
74 52 63 74 19 31
13 31 13 6 68 4
57 36 41 17 40 15
29 59 20 85 73 42
31 67 82 51 44 80
48 41 55 12 15 30
""".trim().lines()

    @Test
    fun testAnswer() {
        assertEquals(110, Year2022Day02.solve(winningNumbers, tickets))
    }
}
