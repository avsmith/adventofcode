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
        replacements.append((old, new))
    else:
        text += line

replacements.sort(key=lambda x: len(x[1]) - len(x[0]), reverse=True)


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


def allreplacements(text):
    allnew = []
    for replacement in replacements:
        allnew += replace(text, replacement[0], replacement[1])
    return allnew


print("Part 1:", len(set(allreplacements(text))))


def find_formula(molecule, steps=0):
    if molecule == "e":
        return steps
    for replace in replacements:
        i = -1
        while True:
            i = molecule.find(replace[1])
            if i == -1:
                break
            new = molecule[:i] + replace[0] + molecule[i + len(replace[1]) :]
            nextsteps = find_formula(new, steps + 1)
            if nextsteps != -1:
                return nextsteps
    return -1


print("Part 2:", find_formula(text))
