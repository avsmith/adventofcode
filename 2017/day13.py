#!/usr/bin/env python

TESTDATA = """\
0: 3
1: 2
4: 4
6: 4
"""

DATA = """\
0: 5
1: 2
2: 3
4: 4
6: 8
8: 4
10: 6
12: 6
14: 8
16: 6
18: 6
20: 12
22: 14
24: 8
26: 8
28: 9
30: 8
32: 8
34: 12
36: 10
38: 12
40: 12
44: 14
46: 12
48: 10
50: 12
52: 12
54: 12
56: 14
58: 12
60: 14
62: 14
64: 14
66: 14
68: 17
70: 12
72: 14
76: 14
78: 14
80: 14
82: 18
84: 14
88: 20
"""

firewall = dict()

for line in DATA.splitlines():
    level, depth = line.split(": ")
    depth = int(depth)
    firewall[level] = depth

toplevel = max([int(i) for i in firewall.keys()])


def traversetime(t):
    return 2 * (t - 1)


def getseverity(fw, delay=0, finalscore=True):
    severity = 0
    for i in range(toplevel + 1):
        if i in [int(k) for k in firewall.keys()]:
            depth = firewall[str(i)]
            if (i + delay) % traversetime(depth) == 0:
                severity += depth * (i + delay)
                if severity > 0 and not finalscore:
                    return 1
    return severity


# delay
print("Star 1: {}".format(getseverity(firewall)))

delay = 0
caught = True
while caught:
    if delay % 100000 == 0:
        print("Delay {}".format(delay))
    if getseverity(firewall, delay, False) > 0:
        delay += 1
    else:
        caught = False

print("Star 2: {}".format(delay))
