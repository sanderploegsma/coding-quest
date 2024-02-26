package com.github.sanderploegsma.codingquest

object Year2022Day02 {
    fun solve(winning: String, tickets: List<String>): Int {
        val winningNumbers = winning.numbers()
        return tickets
            .map { it.numbers() }
            .map { ticket -> ticket.count { winningNumbers.contains(it) } }
            .sumOf {
                when (it) {
                    3 -> 1
                    4 -> 10
                    5 -> 100
                    6 -> 1000
                    else -> 0
                }.toInt()
            }
    }

    private fun String.numbers() = this.split(" ").map { it.toInt() }
}

fun main() {
    val winningNumbers = "12 48 30 95 15 55 97"
    val tickets = Year2022Day02.javaClass.getResource("/2022-02.txt")!!.readText().lines()
    val answer = Year2022Day02.solve(winningNumbers, tickets)
    println("Answer: $answer")
}
