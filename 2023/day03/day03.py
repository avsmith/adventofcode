#!/usr/bin/env python3

import os
import sys
import re
from collections import defaultdict

f = open(os.path.join(sys.path[0], "input03.txt"))
input = f.read()
lines = input.splitlines()


class NestedDefaultDict(defaultdict):
    def __init__(self, *args, **kwargs):
        super(NestedDefaultDict, self).__init__(NestedDefaultDict, *args, **kwargs)

    def __repr__(self):
        return repr(dict(self))


matches = NestedDefaultDict()


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
        # 		print(l, match.group(), match.start(), match.end())
        result = test_id(l, match.start(), match.end())
        # 		print(result, match.group())
        if result:
            score += int(match.group())


print("Part1:", score)
