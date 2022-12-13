#!/usr/bin/env python

import os
import sys

import numpy as np
import networkx as nx

from collections import defaultdict

f = open(os.path.join(sys.path[0], "input12.txt"))
input = f.read()


test = """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi
"""


def pad_with(vector, pad_width, iaxis, kwargs):
    pad_value = kwargs.get("padder", 0)
    vector[: pad_width[0]] = pad_value
    vector[-pad_width[1] :] = pad_value


letters = []

for line in input.splitlines():
    letters.append([x for x in line])
letters = np.array(letters)
letters = np.pad(letters, 1, pad_with)

y, x = np.shape(letters)

g = nx.DiGraph()


def convert_letter(string):
    if string == "S":
        value = ord("a")
    elif string == "E":
        value = ord("z")
    else:
        value = ord(string)
    return value


for i in range(1, x - 1):
    for j in range(1, y - 1):
        start = letters[j, i]
        for jj, ii in [(j - 1, i), (j, i - 1), (j + 1, i), (j, i + 1)]:
            target = letters[jj][ii]
            if (
                convert_letter(target) <= convert_letter(start)
                and convert_letter(target) != 0
            ) or convert_letter(target) == convert_letter(start) + 1:
                if start != "S":
                    start_name = "_".join([start, str(j), str(i)])
                else:
                    start_name = start
                if target != "E":
                    target_name = "_".join([target, str(jj), str(ii)])
                else:
                    target_name = target
                g.add_edge(start_name, target_name)

print("Part1:", nx.dijkstra_path_length(g, source="S", target="E"))

# For part2, the last 'a' will be the best one
# Extract full path and then use the last 'a'
# to find the length. Done by reversing the full path and finding 'a'
reversed_path = list(reversed(nx.dijkstra_path(g, source="S", target="E")))
besta = next((x for x in reversed_path if "a" in x), None)
print("Part2:", nx.dijkstra_path_length(g, source=besta, target="E"))
