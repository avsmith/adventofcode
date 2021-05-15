#!/usr/bin/env python

import os
import sys

from collections import defaultdict

f = open(os.path.join(sys.path[0], "input06.txt"))
input = f.read()

items = input.splitlines()

counts = []

for i in range(len(items[0])):
    counts.append(defaultdict(int))

for line in items:
    for i in range(len(line)):
        counts[i][line[i]] += 1


most = ""
least = ""

for letter in counts:
    most += sorted(letter, key=letter.get, reverse=True)[0]
    least += sorted(letter, key=letter.get, reverse=True)[-1]


print("Part 1:", most)
print("Part 2:", least)
