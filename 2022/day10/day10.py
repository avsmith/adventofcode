#!/usr/bin/env python

import os
import sys

f = open(os.path.join(sys.path[0], "input10.txt"))
input = f.read()

value = 1
result = 0

step = 1

for line in input.splitlines():
    items = line.split()
    instruction = items[0]
    if len(items) == 2:
        amount = int(items[1])
        for _ in range(2):

            if step in (20, 60, 100, 140, 180, 220):
                #                print(step, value, step * value)
                result += step * value
            step += 1

    else:
        amount = 0

        if step in (20, 60, 100, 140, 180, 220):
            #            print(step, value, step * value)
            result += step * value
        step += 1

    value += amount


print(result)
