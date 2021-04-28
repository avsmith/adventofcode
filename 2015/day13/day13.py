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

seating = defaultdict(lambda: defaultdict(int))

for line in cleanedinput.splitlines():
    (persona, happiness, personb) = line.split(" ")
    seating[persona][personb] = int(happiness)

people = set([c for c in seating] + [d for c in seating for d in seating[c]])

happiest = None

for arrangement in permutations(people):
    happy = 0
    guests = len(arrangement)
    for num in range(guests):
        happy += (
            seating[arrangement[num]][arrangement[(num + 1) % guests]]
            + seating[arrangement[(num + 1) % guests]][arrangement[num]]
        )
    if happiest is None or happy > happiest:
        happiest = happy

print(f"Part 1: {happiest}")
