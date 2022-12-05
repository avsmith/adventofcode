#!/usr/bin/env python

import os
import sys

f = open(os.path.join(sys.path[0], "input03.txt"))
input = f.read()


def numbers(c):
    n = ord(c) - 96
    if n > 0:
        return n
    else:
        return n + 32 + 26


test = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
"""

score = 0
for line in input.splitlines():
    overlap = set(line[: len(line) // 2]).intersection(line[len(line) // 2 :])
    score += numbers("".join(overlap))

print(score)
