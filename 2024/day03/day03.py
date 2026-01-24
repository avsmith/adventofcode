#!/usr/bin/env python

import os
import sys
import re

f = open(os.path.join(sys.path[0], "input03.txt"))
input = f.read()

matches = re.findall(r"mul\(\d+,\d+\)", input)

total1 = 0

for a, b in re.findall(r"mul\((\d+),(\d+)\)", input):
    total1 += int(a) * int(b)

print(f"Part 1: {total1}")

do = r"do\(\)"
dont = r"don't\(\)"
mul = r"mul\((\d+),(\d+)\)"
total2 = 0
enabled = True
for x in re.finditer(f'{do}|{dont}|{mul}', input):
    if re.fullmatch(do, x.group()):
        enabled = True
    elif re.fullmatch(dont, x.group()):
        enabled = False
    elif enabled:
        total2 += int(x.group(1)) * int(x.group(2))

print(f"Part 2: {total2}")

