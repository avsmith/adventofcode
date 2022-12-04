#!/usr/bin/env python

import os
import sys

f = open(os.path.join(sys.path[0], "input01.txt"))
input = f.read()

elves = [[int(_) for _ in x.splitlines()] for x in input.split("\n\n")]
calories = [sum(e) for e in elves]

print("Part 1: ", sorted(calories, reverse=True)[0])
print("Part 2: ", sum(sorted(calories, reverse=True)[0:3]))
