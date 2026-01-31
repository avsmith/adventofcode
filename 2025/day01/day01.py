#!/usr/bin/env python3

import os
import sys

testdata = """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82
"""

f = open(os.path.join(sys.path[0], "input.txt"))
data = f.read()

input = data.splitlines()

position = 50
part1times = 0

for c in input:
    direction = c[0]
    value = int(c[1:])

    if direction == "L":
        position -= value
    elif direction == "R":
        position += value
    position %= 100

    # Count times at position zero
    if position == 0:
        part1times += 1

position = 50
part2times = 0

for line in input:

    direction = line[0]
    value = int(line[1:])

    # Split to count full rotations and leave remainder
    full, partial = divmod(value, 100)
    part2times += full

    delta = -partial if direction == "L" else partial
    next_position = position + delta

    if position != 0:
        if direction == "L" and next_position <= 0:
            part2times += 1
        elif direction == "R" and next_position >= 100:
            part2times += 1

    position = next_position % 100

print(f"Part 1: {part1times}")
print(f"Part 2: {part2times}")
