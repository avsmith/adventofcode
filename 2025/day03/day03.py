#!/usr/bin/env python3

import os
import sys

import numpy as np

testdata = """987654321111111
811111111111119
234234234234278
818181911112111
"""

f = open(os.path.join(sys.path[0], "input03.txt"))
data = f.read()

input = data.splitlines()

# [int(d) for d in str(s)]
# a = [12, 4, 3, 7, 8, 10, 22]
# print(np.argmax(a))

tot = 0

for x in input:
    ints = [int(d) for d in x]
    tenspos = np.argmax(ints[:-1])
    digpos = np.argmax(ints[(tenspos + 1) :]) + tenspos + 1
    value = 10 * ints[tenspos] + ints[digpos]
    tot += value

print(tot)
