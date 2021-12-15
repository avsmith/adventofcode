#!/usr/bin/env python

import os
import sys

from collections import defaultdict

f = open(os.path.join(sys.path[0], "test14.txt"))
input = f.read()

template, insertions = input.split("\n\n")

rules = {}

for t in insertions.splitlines():
    source, insert = t.split(" -> ")
    rules[source] = insert

tracker = defaultdict(int)

for i in range(len(template) - 1):
    tracker[template[i : i + 2]] += 1


for _ in range(10):
    newtrack = defaultdict(int)
    for k in tracker:
        newtrack[k[0] + rules[k]] += tracker[k]
        newtrack[rules[k] + k[1]] += tracker[k]
    tracker = newtrack

cc = defaultdict(int)
for k in tracker:
    for c in k:
        cc[c] += tracker[k]
cc[template[0]] += 1
cc[template[-1]] += 1

counts = sorted([cc[k] for k in cc])
print("Part1:", (counts[-1] - counts[0]) // 2)
