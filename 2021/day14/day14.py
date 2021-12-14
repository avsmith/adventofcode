#!/usr/bin/env python

import os
import sys


f = open(os.path.join(sys.path[0], "input14.txt"))
input = f.read()

move, translation = input.split("\n\n")


translate = {}

for t in translation.splitlines():
    ref, out = t.split(" -> ")
    translate[ref] = out

overall = []

for _ in range(10):
    insertion = []
    for i in range(len(move) - 1):
        insertion += translate[move[i : i + 2]]

    newmove = ""
    for i in range(len(insertion)):
        newmove = newmove + move[i] + insertion[i]

    newmove += move[-1]
    move = newmove

    counts = []
    for c in set(move):
        counts.append(move.count(c))

    counts = sorted(counts)


print("Part 1:", counts[-1] - counts[0])

