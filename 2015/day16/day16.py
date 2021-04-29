#!/usr/bin/env python

import sys
import os
from collections import defaultdict

# perl  -ne 'print if !/children: (?!3)/ & !/cats: (?!7)/ & !/samoyeds: (?!2)/ & !/pomeranians: (?!3)/ & !/akitas: (?!0)/ & !/vizslas: (?!0)/ & !/goldfish: (?!5)/ & !/trees: (?!3)/ & !/cars: (?!2)/ & !/perfumes: (?!1)/' 2015/day16/input16.txt

ref = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1,
}


f = open(os.path.join(sys.path[0], "input16.txt"))
input = f.read()


class Sue:
    def __init__(self, args):
        for k in args:
            setattr(self, k, int(args[k]))

    def __getitem__(self, item):
        try:
            return getattr(self, item)
        except AttributeError:
            return None


sues = defaultdict()
# sue 103: cars: 2, perfumes: 1, goldfish: 5
for line in input.splitlines():
    (s, data) = line.replace("Sue ", "").split(": ", 1)
    #    print(data)
    d = {}
    for dat in data.split(", "):
        k, v = dat.split(": ")
        d[k] = v
    sue = Sue(d)
    sues[s] = sue

# print(ref['cars'])
# print(sues)


def check_match(reference, aunt):
    for k in reference:
        if aunt[k] is None:
            continue
        if ref[k] != aunt[k]:
            return False
    return True


def find_aunt(ss):
    for sue in ss:
        if check_match(ref, sues[sue]):
            return sue


print("Part 1:", find_aunt(sues))
