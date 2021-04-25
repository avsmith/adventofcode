#!/usr/bin/env python

DATA = """
2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2
A----------------------------------
    B----------- C-----------
                     D-----
"""

header = "2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2"
items = header.split(" ")
items = [int(x) for x in items]
# print(items)
tot = 0


def read_header(s, metasum):
    print("s", s)
    n_c = s.pop(0)
    n_m = s.pop(0)
    print(n_c, n_m)
    if n_c > 0:
        read_header(s, metasum)
        n_c -= 1
    elif n_c == 0:
        metasum += sum(s[:n_m])
        print("Here", metasum)
        print(s[:n_m])
        s = s[n_m:]
    return metasum


print(read_header(items, tot))
