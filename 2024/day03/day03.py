#!/usr/bin/env python

import os
import sys
import re

f = open(os.path.join(sys.path[0], "input03.txt"))
input = f.read()

test = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"

matches = re.findall(r"mul\(\d+,\d+\)", input)

tot = 0
for m in matches:
    i, j = re.findall(r"\d+", m)
    tot += int(i) * int(j)

print(tot)
