package com.github.sanderploegsma.codingquest

object Year2024Day02 {
    private const val PASSENGER_WIFI_PREFIX = "10.0."
    private const val SHIP_INTERNAL_SYSTEMS_PREFIX = "192.168."

    private data class Packet(val size: Int, val src: String, val dst: String)

    fun solve(input: List<String>): String {
        val packets = input.map(::parse)
        val internalSystems = packets.filter { matchesNetwork(it, SHIP_INTERNAL_SYSTEMS_PREFIX) }.sumOf { it.size }
        val passengerWifi = packets.filter { matchesNetwork(it, PASSENGER_WIFI_PREFIX) }.sumOf { it.size }

        return "$internalSystems/$passengerWifi"
    }

    private fun matchesNetwork(packet: Packet, networkPrefix: String) =
        packet.src.startsWith(networkPrefix) || packet.dst.startsWith(networkPrefix)

    @OptIn(ExperimentalStdlibApi::class)
    private fun parse(line: String): Packet {
        fun extract(range: IntRange): Int {
            val start = (range.first - 1) * 2
            val end = range.last * 2 - 1
            return line.substring(start..end).hexToInt()
        }

        val size = extract(3..4)
        val src = (13..16).map { extract(it..it) }.joinToString(separator = ".")
        val dst = (17..20).map { extract(it..it) }.joinToString(separator = ".")
        return Packet(size, src, dst)
    }
}

fun main() {
    val input = Year2024Day02.javaClass.getResource("/2024-02.txt")!!.readText().lines()
    val answer = Year2024Day02.solve(input)
    println("Answer: $answer")
}
