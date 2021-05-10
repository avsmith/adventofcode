#!/usr/bin/env python

target = 34000000

import numpy as np


def find_house(target, part2=False):
    presents = np.zeros(target)

    if part2:
        for i in range(1, target):
            presents[i : i * 50 : i] += 11 * i
    else:
        for i in range(1, target):
            presents[i::i] += 10 * i

    for i in range(len(presents)):
        if presents[i] >= target:
            return i


print("Part 1:", find_house(target, False))
print("Part 2:", find_house(target, True))
