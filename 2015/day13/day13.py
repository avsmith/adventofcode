#!/usr/bin/env python

import os
import sys
from itertools import permutations
from collections import defaultdict

f = open(os.path.join(sys.path[0], "input13.txt"))
data = f.read()

testdata = """Alice would gain 54 happiness units by sitting next to Bob.
Alice would lose 79 happiness units by sitting next to Carol.
Alice would lose 2 happiness units by sitting next to David.
Bob would gain 83 happiness units by sitting next to Alice.
Bob would lose 7 happiness units by sitting next to Carol.
Bob would lose 63 happiness units by sitting next to David.
Carol would lose 62 happiness units by sitting next to Alice.
Carol would gain 60 happiness units by sitting next to Bob.
Carol would gain 55 happiness units by sitting next to David.
David would gain 46 happiness units by sitting next to Alice.
David would lose 7 happiness units by sitting next to Bob.
David would gain 41 happiness units by sitting next to Carol.
"""

cleanedinput = (
    data.replace("would gain ", "")
    .replace("would lose ", "-")
    .replace("happiness units by sitting next to ", "")
    .replace(".", "")
)

happyscores = defaultdict(lambda: defaultdict(int))

for line in cleanedinput.splitlines():
    (persona, happiness, personb) = line.split(" ")
    happyscores[persona][personb] = int(happiness)

people = set(
    [c for c in happyscores] + [d for c in happyscores for d in happyscores[c]]
)


happiest_guest = None


def seating_score(hs, skip=0):
    people = set([c for c in hs] + [d for c in hs for d in hs[c]])
    happiest = None
    for seating in permutations(people):
        num = len(seating)
        scores = list()
        for i in range(num):
            seatscore = (
                happyscores[seating[i]][seating[(i + 1) % num]]
                + happyscores[seating[(i + 1) % num]][seating[i]]
            )
            scores.append(seatscore)
        happy = sum(sorted(scores)[skip : len(scores)])
        if happiest is None or happy > happiest:
            happiest = happy
    return happiest


print(f"Part 1:", seating_score(happyscores))
print(f"Part 2:", seating_score(happyscores, 1))
