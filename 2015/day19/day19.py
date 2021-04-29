#!/usr/bin/env python


import os
import sys

text = ""
replacements = []
f = open(os.path.join(sys.path[0], "input19.txt"))
input = f.read()

for line in input.splitlines():
    #    print(line)
    if " => " in line:
        (old, new) = line.split(" => ")
        replacements.append({old: new})
    else:
        text += line


def replace(text, old, new):
    found = text.count(old)
    newtext = []
    offset = 0
    for i in range(found):
        begintext = text[:offset]
        endtext = text[offset:]
        foundoff = endtext.find(old)
        newtext.append(begintext + endtext.replace(old, new, 1))
        offset = len(begintext) + foundoff + 1
    return newtext


allnew = []

for replacement in replacements:
    for k in replacement:
        allnew += replace(text, k, replacement[k])

print("Part 1:", len(set(allnew)))
