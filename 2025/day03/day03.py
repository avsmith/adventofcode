#!/usr/bin/env python3

import os
import sys

import numpy as np
import itertools

f = open(os.path.join(sys.path[0], "input03.txt"))
data = f.read()

input = data.splitlines()
        
def find_digit(input, size=2, output=''):
    ints = [int(d) for d in input]
    end = size-len(output)-1
    if end > 0:
        digpos = np.argmax(ints[:-end])
    else:
        digpos = np.argmax(ints)
    output += str(ints[digpos])
    if len(output) == size:
        return output
    else:
        remainder = input[(digpos+1):]
        return(find_digit(remainder, size, output))

part1 = 0
for x in input:
    part1 += int(find_digit(x))
print("Part1:", part1)

part2 = 0
for x in input:
    part2 += int(find_digit(x,12))
print("Part2:", part2)
           