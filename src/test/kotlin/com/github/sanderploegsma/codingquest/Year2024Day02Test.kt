package com.github.sanderploegsma.codingquest

import kotlin.test.Test
import kotlin.test.assertEquals

class Year2024Day02Test {
    private val example = """
45000377000000008306f39f0A000bc1d7253441
4500007f0000000005065de1c0a800b833c555ee
450002e50000000008061ef5c0a8796698721661
4500017e00000000b206e54e88c7fd4f0A00244c
45000164000000009d06d73c0A0000b7e0b143b8
""".trim().lines()

    @Test
    fun testAnswer() {
        assertEquals("868/1625", Year2024Day02.solve(example))
    }
}
