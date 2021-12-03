#!/usr/bin/env python

import os
import sys

f = open(os.path.join(sys.path[0], "input03.txt"))
input = f.read()

data = [int(x,2) for x in input.splitlines()]


def bit_set(list, bit):
    count = 0
    for x in list:
        if x & (1 << bit):
            count += 1
    if count > len(list)/2:
        return True


gamma = 0
epsilon = 0

for x in range(max(data).bit_length(), 0, -1):
    if bit_set(data, x-1):
        gamma ^= 2**(x-1)
    else:
        epsilon ^= 2**(x-1)

print("Part 1:", gamma*epsilon)
