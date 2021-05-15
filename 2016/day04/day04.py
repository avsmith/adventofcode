#!/usr/bin/env python

import os
import sys

from collections import defaultdict

f = open(os.path.join(sys.path[0], "input04.txt"))
input = f.read()

legal = 0


def convert_word(word, rotate):
    new = ""
    for x in word:
        let = ord(x) - 97 + rotate
        new += chr(let % 26 + 97)
    return new


part2 = None

for line in input.splitlines():
    items = line.split("-")
    sector = int(items[-1][0 : len(items[-1]) - 7])
    checksum = items[-1][len(items[-1]) - 6 : len(items[-1]) - 1]
    counts = defaultdict(int)
    for word in items[0:-1]:
        for c in word:
            counts[c] += 1
    letters = sorted([(k, counts[k]) for k in counts], key=lambda x: (-x[1], x[0]))
    calculated = "".join([letters[i][0] for i in range(5)])

    if calculated == checksum:
        legal += sector
    if (
        " ".join([convert_word(w, sector) for w in items[0:-1]])
        == "northpole object storage"
    ):
        part2 = sector


print("Part 1:", legal)
print("Part 2:", part2)
