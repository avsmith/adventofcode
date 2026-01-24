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
bl
times = 0
position = 50

for c in input:
    direction = c[0]
    value = int(c[1:])

    if direction == "L":
        position -= value
    elif direction == "R":
        position += value


    position %= 100

    if position == 0:
        times += 1


print(times)
