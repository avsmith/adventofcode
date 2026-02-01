#!/usr/bin/env python3

from pathlib import Path
import portion as p

text = Path("input05.txt").read_text()


interval_text, value_text = text.split("\n\n")

interval_set = p.empty()

for line in interval_text.splitlines():
	left, right = map(int, line.split("-"))
	interval_set |= p.closed(left, right)

count_values_in_intervals = 0
for v in map(int, value_text.splitlines()):
	if v in interval_set:
		count_values_in_intervals += 1

print(count_values_in_intervals)

interval_size = 0
for interval in interval_set:
	interval_size += interval.upper - interval.lower + 1

print(interval_size)
