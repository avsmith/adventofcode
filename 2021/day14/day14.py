#!/usr/bin/env python

import os
import sys

from collections import defaultdict

f = open(os.path.join(sys.path[0], "test14.txt"))
input = f.read()

# Separate template and the insertion rules
template, insertions = input.split("\n\n")

# Rules for character insertion
rules = {}

# Read rules into dictionary
for t in insertions.splitlines():
    source, insert = t.split(" -> ")
    rules[source] = insert


def pair_insertions(moves=10):

    # Counter for pairs of characters
    tracker = defaultdict(int)

    # Seed the counter
    for i in range(len(template) - 1):
        tracker[template[i : i + 2]] += 1

    # Do insertions by adding to the tracking counter
    # rather than building huge string
    for _ in range(moves):
        newtrack = defaultdict(int)
        # For each starting character pair
        # count the insertions
        for k in tracker:
            newtrack[k[0] + rules[k]] += tracker[k]
            newtrack[rules[k] + k[1]] += tracker[k]
        tracker = newtrack
    return tracker


def polymer_char_counts(move=10):
    tracker = pair_insertions(move)

    charcounts = defaultdict(int)
    for pair in tracker:
        for char in pair:
            charcounts[char] += tracker[pair]
    # Add one for the first and last starting char
    # charcounts will then be 2x the results
    charcounts[template[0]] += 1
    charcounts[template[-1]] += 1

    counts = sorted([charcounts[k] for k in charcounts])
    return (counts[-1] - counts[0]) // 2


print("Part 1:", polymer_char_counts(10))
print("Part 2:", polymer_char_counts(40))
