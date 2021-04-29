#!/usr/bin/env python

from itertools import combinations

buckets = [11, 30, 47, 31, 32, 36, 3, 1, 5, 3, 32, 36, 15, 11, 46, 26, 28, 1, 19, 3]
target = 150


def number_combos(containers, total, min=False):
    possibilities = 0
    min_containers = None
    min_possibilities = 0
    for i in range(1, len(containers)):
        for combo in list(combinations(containers, i)):
            if sum(combo) == total:
                possibilities += 1
                if min and (min_containers is None or len(combo) < min_containers):
                    min_containers = len(combo)
                    min_possibilities = 1
                elif min and len(combo) == min_containers:
                    min_possibilities += 1
    if min:
        return min_possibilities
    return possibilities


print("Part 1: ", number_combos(buckets, target))
print("Part 2: ", number_combos(buckets, target, True))
