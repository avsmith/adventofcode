#!/usr/bin/env python3

import os
import sys

f = open(os.path.join(sys.path[0], "input05.txt"))
input = f.read()

test = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
"""

seeds = []
maps = {}


class Seedmap:
    def __init__(self, mtype, destrange, sourcerange, rangelength):
        origin, destination = mtype.split("-to-")
        self.mtype = mtype
        self.destination = destination
        self.sourcerange = int(sourcerange)
        self.destrange = int(destrange)
        self.rangelength = int(rangelength)

    def evaluate(self, value):
        if value >= self.start and value <= self.start + self.length:
            return self.score
        else:
            return False

    def __str__(self):
        string = f"""Type: {self.mtype}
Source range: {self.sourcerange}
Dest range: {self.destrange}
Length: {self.rangelength}
"""
        return string

    def findvalue(self, input):
        if input >= self.sourcerange and input < self.sourcerange + self.rangelength:
            return (self.destination, input - self.sourcerange + self.destrange)
        else:
            return (self.destination, input)


mtype = ""
items = []

for line in input.splitlines():
    if line.startswith("seeds: "):
        line = line.removeprefix("seeds: ")
        seeds = [int(x) for x in line.split()]
    if "map" in line:
        if len(items) > 0:
            maps[origin] = items
        items = []
        mtype = line
        mtype = mtype.replace(" map:", "")
        origin, dest = mtype.split("-to-")
    splits = line.split()
    if len(splits) == 3:
        item = Seedmap(mtype, *splits)
        items.append(item)
maps[origin] = items


def get_value(test, input):
    current = input
    for m in maps[test]:
        next, value = m.findvalue(input)
        if value != input:
            current = value
    return (next, current)


def trace_map(test, input):
    next, value = get_value(test, input)
    if next in maps.keys():
        next, value = trace_map(next, value)
    return next, value


values = []
for seed in seeds:  #
    current = "seed"
    what, value = trace_map(current, seed)
    values.append(value)

print(sorted(values)[0])
