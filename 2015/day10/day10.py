#!/usr/bin/env python

import re

input = "1113222113"


def split_count(txt):
    res = [iters.group(0) for iters in re.finditer(r"(\d)\1*", txt)]
    ret = ""
    for x in res:
        ret += str(len(x)) + str(x)[0]
    return ret


def wrap_split(txt, rounds=40):
    txt
    for i in range(rounds):
        txt = split_count(txt)
    return txt


print(len(wrap_split(input)))
