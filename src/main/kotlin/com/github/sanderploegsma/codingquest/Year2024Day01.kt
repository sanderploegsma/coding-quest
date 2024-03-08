package com.github.sanderploegsma.codingquest

import kotlin.math.pow
import kotlin.math.sqrt

object Year2024Day01 {
    fun solve(input: List<String>) = input
        .map(::parse)
        .groupBy { it.first }
        .minOf { it.value.sumOf(Pair<String,Int>::second) }

    private fun parse(line: String): Pair<String, Int> {
        val (id, type, value) = line.split(' ')
        return when (type) {
            "Discount", "Rebate" -> id to -value.toInt()
            else -> id to value.toInt()
        }
    }
}

fun main() {
    val input = Year2024Day01.javaClass.getResource("/2024-01.txt")!!.readText().lines()
    val answer = Year2024Day01.solve(input)
    println("Answer: $answer")
}
