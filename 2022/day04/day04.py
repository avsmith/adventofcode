#!/usr/bin/env python

import os
import sys
import re

f = open(os.path.join(sys.path[0], "input04.txt"))
input = f.read()


def contained(a, b):
    if (a[0] >= b[0] and a[1] <= b[1]) or (b[0] >= a[0] and b[1] <= a[1]):
        return True
    return False


def overlaps(a, b):
    if a[1] >= b[0] and b[1] >= a[0]:
        return True
    return False


within = 0
overs = 0
for line in input.splitlines():
    nums = [int(s) for s in re.findall(r"\b\d+\b", line)]

    within += contained(nums[:2], nums[2:])
    overs += overlaps(nums[:2], nums[2:])


print("Part1:", within)
print("Part2:", overs)
