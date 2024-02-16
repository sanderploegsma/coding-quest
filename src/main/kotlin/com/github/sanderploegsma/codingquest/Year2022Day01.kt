package com.github.sanderploegsma.codingquest

object Year2022Day01 {
    fun solve(input: String) =
        input.lineSequence()
            .map { it.toInt() }
            .windowed(60, transform = { it.average() })
            .count { it < 1500 || it > 1600 }
}

fun main() {
    val input = Year2022Day01.javaClass.getResource("/2022-01.txt")!!.readText()
    val answer = Year2022Day01.solve(input)
    println("Answer: $answer")
}
