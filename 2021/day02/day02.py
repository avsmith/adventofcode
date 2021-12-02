#!/usr/bin/env python

import os
import sys

f = open(os.path.join(sys.path[0], "input02.txt"))
input = f.read()

data = [x.split() for x in input.splitlines()]

height = 0
lateral = 0


for move, dist in data:
    if move == 'up':
        height -= int(dist)
    elif move == 'down':
        height += int(dist)
    elif move == 'forward':
        lateral += int(dist)

print("Part 1:", height*lateral)

