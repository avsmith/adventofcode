#!/usr/bin/env python


import os
import sys

f = open(os.path.join(sys.path[0], "input10.txt"))
input = f.read().rstrip()

testinput = """
value 5 goes to bot 2
bot 2 gives low to bot 1 and high to bot 0
value 3 goes to bot 1
bot 1 gives low to output 1 and high to bot 0
bot 0 gives low to output 2 and high to output 0
value 2 goes to bot 2
"""
lines = input.splitlines()

rules = [None] * 210
values = [None] * 210

for line in lines:
    items = line.split()
    if len(items) == 12:
        rules[int(items[1])] = (int(items[6]), int(items[11]))
    elif len(items) == 6:
        if isinstance(values[int(items[5])], list):
            values[int(items[5])].append(int(items[1]))
            values[int(items[5])].sort()
        else:
            values[int(items[5])] = [int(items[1])]


def bots(val, rules):
    changes = [(i, x) for i, x in enumerate(values) if x is not None and len(x) > 1]
    while len(changes) > 0:
        for change in changes:
            donor = change[0]
            lowvalue = change[1][0]
            highvalue = change[1][1]
            if lowvalue == 17 and highvalue == 61:
                return donor
            lowrecipient = rules[donor][0]
            highrecipient = rules[donor][1]
            if isinstance(values[lowrecipient], list):
                values[lowrecipient].append(lowvalue)
                values[lowrecipient].sort()
            else:
                values[lowrecipient] = [lowvalue]
            if isinstance(values[highrecipient], list):
                values[highrecipient].append(highvalue)
                values[highrecipient].sort()
            else:
                values[highrecipient] = [highvalue]
            values[donor] = []
        changes = [(i, x) for i, x in enumerate(values) if x is not None and len(x) > 1]
    return None


print("Part 1:", bots(values, rules))
