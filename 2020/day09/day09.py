#!/usr/bin/env python

import itertools
import numpy as np

testinput = """35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576
"""

import os, sys

f = open(os.path.join(sys.path[0], "input09.txt"))
input = f.read()

data = [int(x) for x in input.splitlines()]
offset = 25


def not_sum(array, delta):
    while True:
        for i in range(len(array) - delta):
            summed = set(
                [
                    a + b
                    for a, b in list(itertools.combinations(array[i : i + delta], 2))
                ]
            )
            if array[i + delta] not in summed:
                return array[i + delta]


def find_contiguous(array, value):
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            continuous_sum = np.sum(array[i:j])
            if continuous_sum > value:
                break
            elif continuous_sum == value:
                return min(array[i:j]) + max(array[i:j])


part1 = not_sum(data, 25)
print(part1)
part2 = find_contiguous(data, part1)
print(part2)
