#!/usr/bin/env python

import os
import sys

f = open(os.path.join(sys.path[0], "input03.txt"))
input = f.read()


def numbers(c):
    n = ord(c) - 96
    if n > 0:
        return n
    else:
        return n + 32 + 26


def overlapping(x):
    overlaps = set(x[0])
    for i in range(1, len(x)):
        overlaps = overlaps.intersection(set(x[i]))
    return "".join(overlaps.difference(set("\n")))


score = 0
for line in input.splitlines():
    overlap = set(line[: len(line) // 2]).intersection(line[len(line) // 2 :])
    score += numbers("".join(overlap))

print("Part1:", score)

from itertools import islice

score2 = 0
with open("input03.txt") as f:
    while True:
        next_n_lines = list(islice(f, 3))
        #        print(next_n_lines, "\n")
        if len(next_n_lines) > 2:
            score2 += numbers(overlapping(next_n_lines))
        if not next_n_lines:
            break

print("Part2:", score2)
