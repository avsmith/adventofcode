#!/usr/bin/env python

import os
import sys

f = open(os.path.join(sys.path[0], "input01.txt"))
input = f.read()

data = [int(x) for x in input.splitlines()]

count1 = 0

for i in range(1, len(data)):
    if data[i] < data[i+1]:
        count1 += 1

print("Part 1", count1)
