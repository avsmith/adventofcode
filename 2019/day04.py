#!/usr/bin/env python

from itertools import groupby


count1 = 0
count2 = 0

for i in range(264360, 746325 + 1):
    digits = [int(d) for d in str(i)]
    res_inc = all(i <= j for i, j in zip(digits, digits[1:]))
    res_adj = any(i == j for i, j in zip(digits, digits[1:]))
    res_doubles = 2 in [sum(1 for _ in group) for _, group in groupby(digits)]
    if res_inc and res_adj:
        count1 += 1
        if res_doubles:
            count2 += 1

print(count1, count2)
