#!/usr/bin/env python

import os
import sys

f = open(os.path.join(sys.path[0], "input08.txt"))
input = f.read()

total = 0
for line in input.splitlines():
    inwires, outwires = line.split(" | ")
    for outwire in outwires.split(" "):
        connections = len(outwire)
        if connections in [2, 3, 4, 7]:
            total += 1

print(total)
