package com.github.sanderploegsma.codingquest

import kotlin.math.pow
import kotlin.math.sqrt

object Year2022Day03 {
    fun solve(input: List<String>) = input
        .map { it.numbers() }
        .windowed(2)
        .sumOf { (a, b) ->
            val (x1, y1, z1) = a
            val (x2, y2, z2) = b
            sqrt((x2 - x1).squared + (y2 - y1).squared + (z2 - z1).squared).toInt()
        }

    private val Int.squared get() = toDouble().pow(2)

    private fun String.numbers() = this.split(" ").map { it.toInt() }
}

fun main() {
    val input = Year2022Day03.javaClass.getResource("/2022-03.txt")!!.readText().lines()
    val answer = Year2022Day03.solve(input)
    println("Answer: $answer")
}
