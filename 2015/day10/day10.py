#!/usr/bin/env python

import re

input = "1113222113"


def split_count(txt):
    splittxt = [iters.group(0) for iters in re.finditer(r"(\d)\1*", txt)]
    ret = ""
    for x in splittxt:
        ret += str(len(x)) + str(x)[0]
    return ret


def wrap_split(txt, rounds=40):
    for i in range(rounds):
        txt = split_count(txt)
    return txt


print("Part 1:", len(wrap_split(input)))
print("Part 2:", len(wrap_split(input, 50)))
