#!/usr/bin/env python

import os
import sys
import json

with open(os.path.join(sys.path[0], "input12.json")) as f:
    j = json.load(f)
f.close()


def extract_value(item, red=False):
    if isinstance(item, int):
        return item
    elif isinstance(item, list):
        val = 0
        for n in item:
            val += extract_value(n, red)
        return val
    elif isinstance(item, dict):
        if red and ("red" in item.values() or "red" in item):
            return 0
        val = 0
        for k in item:
            val += extract_value(k, red)
            val += extract_value(item[k], red)
        return val
    else:
        return 0


print("Part 1:", extract_value(j, red=False))
print("Part 2:", extract_value(j, red=True))
