#!/usr/bin/env python

import re
from collections import defaultdict

DATA = """\
#1 @ 1,3: 4x4
#2 @ 3,1: 4x4
#3 @ 5,5: 2x2
"""

with open("day03.txt", "r") as fh:
    lines = [line.strip() for line in fh.readlines()]

# d = defaultdict(lambda: defaultdict(int))
d = defaultdict(int)
re.compile("#(\d+)")
for code in lines:
    id, instruct = code.split(" @ ")
    start, pos = instruct.split(": ")
    x, y = start.split(",")
    w, h = pos.split("x")
    x = int(x)
    y = int(y)
    for xd in range(int(w)):
        for yd in range(int(h)):
            d[x + xd, y + yd] += 1

tot = 0
for e in d:
    if d[e] > 1:
        tot += 1
print(tot)

for code in lines:
    id, instruct = code.split(" @ ")
    start, pos = instruct.split(": ")
    x0, y0 = start.split(",")
    xd, yd = pos.split("x")
    x0 = int(x0)
    y0 = int(y0)
    clean = True
    for x in range(int(xd)):
        for y in range(int(yd)):
            if d[x0 + x, y0 + y] > 1:
                clean = False
    if clean:
        print(id)
