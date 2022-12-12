#!/usr/bin/env python

import os
import sys

f = open(os.path.join(sys.path[0], "input20.txt"))
input = f.read()

ranges = []

for line in input.splitlines():
    start, stop = line.split("-")
    ranges.append((int(start), int(stop)))

# Taken from https://codereview.stackexchange.com/questions/21307/consolidate-list-of-ranges-that-overlap
def remove_overlap(ranges):
    result = []
    current_start = -1
    current_stop = -1

    for start, stop in sorted(ranges):
        if start > current_stop:
            # this segment starts after the last segment stops
            # just add a new segment
            current_start, current_stop = start, stop
            result.append((start, stop))
        else:
            # segments overlap, replace
            # current_start already guaranteed to be lower
            current_stop = max(current_stop, stop)
            result[-1] = (current_start, current_stop)

    return result


simplified = remove_overlap(ranges)

for i in range(1, len(simplified)):
    if simplified[i - 1][1] + 1 != simplified[i][0]:
        print("Part1:", simplified[i - 1][1] + 1)
        break

allowed = 0

for i in range(1, len(simplified)):
    allowed += simplified[i][0] - simplified[i - 1][1] - 1

print("Part2:", allowed)
