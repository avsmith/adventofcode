#!/usr/bin/env python

import os, sys

f = open(os.path.join(sys.path[0], "day09.txt"))

text = f.read()

TESTDATA = """\
{}
{{{}}}
{{},{}}
{{{},{},{{}}}}
{<a>,<a>,<a>,<a>}
{{<ab>},{<ab>},{<ab>},{<ab>}}
{{<!!>},{<!!>},{<!!>},{<!!>}},
{{<a!>},{<a!>},{<a!>},{<ab>}}
"""

import re


def bookmark():
    return False


# Match exclamation marks and following
p_exclaim = re.compile("!.")
# Clean out that text
cleaned = p_exclaim.sub("", text)


curscore = 1
runningscore = 0
garbagescore = 0
garbage = False

split_cleaned = list(cleaned)

for i in range(len(split_cleaned)):
    curchar = split_cleaned[i]
    if not garbage and curchar == "<":
        garbage = True
        continue
    if garbage and curchar != ">":
        garbagescore += 1
        continue
    if garbage and curchar == ">":
        garbage = False
        continue
    if curchar == "{":
        runningscore += curscore
        curscore += 1
    if curchar == "}":
        curscore -= 1

print("Answer star 1: {}".format(runningscore))
print("Answer star 2: {}".format(garbagescore))
