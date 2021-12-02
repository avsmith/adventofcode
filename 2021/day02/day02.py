#!/usr/bin/env python

import os
import sys

f = open(os.path.join(sys.path[0], "input02.txt"))
input = f.read()

data = [x.split() for x in input.splitlines()]


def move_sub(data, part2=False):
    depth = 0
    lateral = 0
    for move, dist in data:
        dist = int(dist)
        if move == 'up':
            depth -= dist
        elif move == 'down':
            depth += dist
        elif move == 'forward':
            lateral += dist
    return(depth*lateral)


print("Part 1:", move_sub(data))
