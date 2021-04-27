#!/usr/bin/env python

import os
import sys
from itertools import permutations
from collections import defaultdict

testdata = """London to Dublin = 464
London to Belfast = 518
Dublin to Belfast = 141
"""

f = open(os.path.join(sys.path[0], "input09.txt"))
data = f.read()
rts = defaultdict(lambda: defaultdict(int))

for line in data.splitlines():
    (citya, to, cityb, operator, distance) = line.split(" ")
    rts[citya][cityb] = int(distance)

cities = set([c for c in rts] + [d for c in rts for d in rts[c]])

shortdist = None
longdist = None

for path in permutations(cities):
    length = 0
    for num in range(len(path) - 1):
        length += rts[path[num]][path[num + 1]] + rts[path[num + 1]][path[num]]
    if shortdist is None or length < shortdist:
        shortdist = length
    if longdist is None or length > longdist:
        longdist = length

print(f"Part 1: {shortdist}")
print(f"Part 2: {longdist}")
