#!/usr/bin/env python

import os
import sys

f = open(os.path.join(sys.path[0], "input08.txt"))
input = f.read()

total = 0
total2 = 0


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


def define_wires(wires):
    decoder = dict()
    lettercodes = wires.split(" ")
    # Sort the observed wires by size
    # They end in the order
    # 1, 7, 4, [2, 3, 4], [0, 6, 9], 8
    lettercodes.sort(key=lambda s: len(s))
    counter = dict()
    for letter in "abcdefg":
        counts = inwires.count(letter)
        counter[letter] = counts
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
    decoder["a"] = list(set(lettercodes[1]) - set(lettercodes[0]))[0]
    # The letter seen overall 4 times is segment e
    decoder["e"] = [k for k in counter if counter[k] == 4][0]
    # The letter seen overall 6 times is segment b
    decoder["b"] = [k for k in counter if counter[k] == 6][0]
    # The letter seen overall 9 times is segement f
    decoder["f"] = [k for k in counter if counter[k] == 9][0]
    # For the number 1, since we know segment f, we can determine c
    decoder["c"] = list(set(lettercodes[0]) - set(decoder["f"]))[0]
    # For the number 4, we know segments b,c,f and can determine d
    decoder["d"] = list(set(lettercodes[2]) - set([decoder[x] for x in "bcf"]))[0]
    # We know all codes a,b,c,d,e,f and can determine g
    decoder["g"] = list(set(lettercodes[-1]) - set([decoder[x] for x in "abcdef"]))[0]
    # Return translation table
    return decoder


def make_decoder(wiredef):
    answers = dict()
    for word in reference_segments:
        observed_segments = "".join(sorted([wiredef[x] for x in word]))
        answers[observed_segments] = reference_segments[word]
    return answers


for line in input.splitlines():
    inwires, outwires = line.split(" | ")
    for outwire in outwires.split(" "):
        connections = len(outwire)
        if connections in [2, 3, 4, 7]:
            total += 1
    counter = dict()
    for letter in "abcdefg":
        counts = inwires.count(letter)
        counter[letter] = counts
    magic = make_decoder(define_wires(inwires))
    code = ""
    for outwire in outwires.split(" "):
        outwire = "".join(sorted(outwire))
        code += str(magic[outwire])
    total2 += int(code)

print("Part 1:", total)
print("Part 2:", total2)
