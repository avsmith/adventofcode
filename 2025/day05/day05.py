#!/usr/bin/env python3

from pathlib import Path
import portion as p

text = Path("input05.txt").read_text()

test = """3-5
10-14
16-20
12-18

1
5
8
11
17
32
"""

intervals, values = text.split("\n\n")

interval_set = p.empty()

for interval in intervals.splitlines():
	left, right = interval.split("-")
	interval_set =  interval_set | p.closed(int(left),int(right))

fresh = 0

for v in values.splitlines():
	v = int(v)
	if v in interval_set:
		fresh+= 1
		
print(fresh)

fresh2 = 0
for i in interval_set:
	fresh2 += i.upper-i.lower+1
	
print(fresh2)