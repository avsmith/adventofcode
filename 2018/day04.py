#!/usr/bin/env python

import re
from collections import defaultdict


def nested_dict(n, type):
    if n == 1:
        return defaultdict(type)
    else:
        return defaultdict(lambda: nested_dict(n - 1, type))


with open("day04.txt", "r") as fh:
    lines = sorted([line.strip() for line in fh.readlines()])

mainre = re.compile("\[(\d{4})-(\d{2})-(\d{2}) (\d{2}):(\d{2})\] ([^\n]+)")
guard = re.compile("Guard #(\d+) begins shift")

id = "#0"
start = 0
d = nested_dict(2, int)

for line in lines:
    year, month, day, hour, minute, instruct = mainre.match(line).groups()
    m = guard.match(instruct)
    if m:
        id = int(m.group(1))
    elif instruct == "falls asleep":
        start = int(minute)
    elif instruct == "wakes up":
        for x in range(start, int(minute)):
            d[id][x] += 1

# print(d)
ID = 0
maxsleep = 0

for id in d:
    sleeping = 0
    for min in d[id]:
        sleeping += d[id][min]
    if sleeping > maxsleep:
        maxsleep = sleeping
        ID = id

sleepiest = 0
minutes = 0
for min in d[ID]:
    if d[ID][min] > sleepiest:
        sleepiest = d[ID][min]
        minutes = min

print(minutes * ID)

guard = 0
minsleep = 0
sleepmin = 0
IDx = 0

for id in d:
    for min in d[id]:
        if d[id][min] > minsleep:
            minsleep = d[id][min]
            sleepmin = min
            IDx = id

print(IDx * sleepmin)
