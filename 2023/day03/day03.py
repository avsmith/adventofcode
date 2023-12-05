#!/usr/bin/env python3

import os
import sys
import re
from collections import defaultdict

f = open(os.path.join(sys.path[0], "input03.txt"))
input = f.read()
lines = input.splitlines()


# Borrowed
class NestedDefaultDict(defaultdict):
    def __init__(self, *args, **kwargs):
        super(NestedDefaultDict, self).__init__(NestedDefaultDict, *args, **kwargs)

    def __repr__(self):
        return repr(dict(self))


matches = NestedDefaultDict()
gears = NestedDefaultDict()


test = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
"""

# lines = input.splitlines()

for l in range(len(lines)):
    for match in re.finditer(r"[^\.\d]", lines[l]):
        # 		print(l, match.group(), match.start(), match.end())
        matches[l][match.start()] = True


def test_id(line, start, end):
    for l in range(line - 1, line + 2):
        for p in range(start - 1, end + 1):
            if matches[l][p]:
                return True
    return False


score = 0


for l in range(len(lines)):
    for match in re.finditer(r"\d+", lines[l]):
        result = test_id(l, match.start(), match.end())

        for x in range(match.start(), match.end()):
            gears[l][x] = int(match.group())
        if result:
            score += int(match.group())


print("Part1:", score)

matched = list()

score2 = 0

for l, vals in matches.items():
    for pos, match in vals.items():
        if match:
            matched = list()
            for x in range(l - 1, l + 2):
                for y in range(pos - 1, pos + 2):
                    if isinstance(gears[x][y], int):
                        matched.append(gears[x][y])
            # This finds unique gears
            # Will break if there are two different
            # Gears with the same value
            # Worked as a solution
            matched = list(set(matched))
            if len(matched) == 2:
                score2 += matched[0] * matched[1]

print("Part2:", score2)
