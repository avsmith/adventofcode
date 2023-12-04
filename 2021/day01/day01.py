#!/usr/bin/env python

import os
import sys

f = open(os.path.join(sys.path[0], "input01.txt"))
input = f.read()

data = [int(x) for x in input.splitlines()]


def deeper(depths, window=1):
    decreasing = 0
    for i in range(window, len(depths)):
        if sum(depths[i - window : i]) < sum(depths[i - window + 1 : i + 1]):
            decreasing += 1
    return decreasing


print("Part 1:", deeper(data))
print("Part 2:", deeper(data, 3))
