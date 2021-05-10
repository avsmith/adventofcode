#!/usr/bin/env python

input = """1
3
5
11
13
17
19
23
29
31
41
43
47
53
59
61
67
71
73
79
83
89
97
101
103
107
109
113
"""

testinput = """1
2
3
4
5
7
8
9
10
11
"""

numbers = [int(x) for x in input.splitlines()]


import itertools
import numpy as np


def has_sum(nums, target, minsize):
    for i in range(minsize, len(nums) - minsize):
        for combo in itertools.combinations(nums, i):
            if sum(combo) == target:
                return True


def find_legal_combos(nums, split=3):
    # Define the target package sum
    target = sum(nums) / split
    # Only start with minimum possible combo size
    minsize = int(1 + target // max(nums))
    for i in range(minsize, len(nums) - minsize):
        possible = list()
        for combo in itertools.combinations(nums, i):
            if sum(combo) == target:
                remaining = [n for n in nums if not n in combo]
                # Test if the same sum can be found in the remaining numbers
                if has_sum(remaining, target, minsize):
                    possible.append(list(combo))

        if len(possible) > 0:
            qe = None
            for x in possible:
                if qe is None or np.prod(x) < qe:
                    qe = np.prod(x)
            return qe


print("Part 1:", find_legal_combos(numbers))
print("Part 2:", find_legal_combos(numbers, 4))
