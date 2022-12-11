#!/usr/bin/env python

import os
import sys

f = open(os.path.join(sys.path[0], "input10.txt"))
input = f.read()

value = 1
result = 0

step = 1

terminal = ["" for _ in range(6)]

for line in input.splitlines():
    items = line.split()
    instruction = items[0]
    if len(items) == 2:
        amount = int(items[1])
        for _ in range(2):
            row = (step - 1) // 40
            if step in (20, 60, 100, 140, 180, 220):
                result += step * value
            if step - 40 * row in range(value, value + 3):
                terminal[row] += "#"
            else:
                terminal[row] += "."
            step += 1
    else:
        amount = 0
        # This bit nearly duplicated that above
        # Should be turned into a function for both
        row = (step - 1) // 40
        if step in (20, 60, 100, 140, 180, 220):
            result += step * value
        if step - 40 * row in range(value, value + 3):
            terminal[row] += "#"
        else:
            terminal[row] += "."
        step += 1

    value += amount

print("Part1:", result)
# Need to read this to letters
print("Part2:")
print("\n".join(terminal))
