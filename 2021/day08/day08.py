#!/usr/bin/env python

import os
import sys

from collections import defaultdict

f = open(os.path.join(sys.path[0], "input08.txt"))
input = f.read()

reference_segments = {
    "abcefg": 0,
    "cf": 1,
    "acdeg": 2,
    "acdfg": 3,
    "bcdf": 4,
    "abdfg": 5,
    "abdefg": 6,
    "acf": 7,
    "abcdefg": 8,
    "abcdgf": 9,
}


def count_segments(wires):
    segment_counts = defaultdict(int)
    for wire in wires:
        for let in wire:
            segment_counts[let] += 1
    return segment_counts


def wire_totals(wires):
    segment_counts = count_segments(wires)
    wire_count = defaultdict(int)
    for wire in wires:
        for let in wire:
            wire_count[wire] += segment_counts[let]
    return wire_count


# Based on reddit comment, there is a simple algorithm
# If you count the number of segments by letter overall
# and then sum over each pattern, tne numbers are unique
reference_totals = wire_totals(reference_segments.keys())

# Then make a reference with total is key with the output number
reference_counts = dict()
for value, word in enumerate(reference_segments):
    reference_counts[reference_totals[word]] = value

# Previous strategy
# Used a set of rules to determine wires
# Much simple solution now

# Rules for determining positions of seven segment display
#  aaaa
# b    c
# b    c
#  dddd
# e    f
# e    f
#  gggg

# Codes for numbers
# 0 abcefg
# 1 cf
# 2 acdeg
# 3 acdfg
# 4 bcdf
# 5 abdfg
# 6 abdefg
# 7 acf
# 8 abcdefg
# 9 abcdgf

# Overall count of segments on
# a 8
# b 6
# c 8
# d 7
# e 4
# f 9
# g 7

# Lettercodes are sorted by code length
# The letter seen in 7 but not 1 is segment a
# decoder["a"] = list(set(lettercodes[1]) - set(lettercodes[0]))[0]
# The letter seen overall 4 times is segment e
# decoder["e"] = [k for k in counter if counter[k] == 4][0]
# The letter seen overall 6 times is segment b
# decoder["b"] = [k for k in counter if counter[k] == 6][0]
# The letter seen overall 9 times is segement f
# decoder["f"] = [k for k in counter if counter[k] == 9][0]
# For the number 1, since we know segment f, we can determine c
# decoder["c"] = list(set(lettercodes[0]) - set(decoder["f"]))[0]
# For the number 4, we know segments b,c,f and can determine d
# decoder["d"] = list(set(lettercodes[2]) - set([decoder[x] for x in "bcf"]))[0]
# We know all codes a,b,c,d,e,f and can determine g
# decoder["g"] = list(set(lettercodes[-1]) - set([decoder[x] for x in "abcdef"]))[0]


def count_patterns(wires):
    wires = wires.split(" ")
    wires = ["".join(sorted(x)) for x in wires]
    wire_counts = wire_totals(wires)
    return wire_counts


total = 0
total2 = 0

for line in input.splitlines():
    inwires, outwires = line.split(" | ")
    magic_decoder = count_patterns(inwires)
    code = ""
    for outwire in outwires.split(" "):
        connections = len(outwire)
        if connections in [2, 3, 4, 7]:
            total += 1
        outwire = "".join(sorted(outwire))
        code += str(reference_counts[magic_decoder[outwire]])
    total2 += int(code)

print("Part 1:", total)
print("Part 2:", total2)
