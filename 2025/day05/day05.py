#!/usr/bin/env python3

from pathlib import Path
import portion as p

inputtext = Path("input05.txt").read_text()

def parse_intervals(text):
	interval_set = p.empty()
	for left, right in (map(int, l.split("-")) for l in text.splitlines()):
		interval_set |= p.closed(left, right)
	return interval_set


def count_values(interval_set, values):
	return sum(int(v) in interval_set for v in values.splitlines())


def interval_size(interval_set):
	return sum(i.upper - i.lower + 1 for i in interval_set)


interval_text, value_text = inputtext.split("\n\n")

interval_set = parse_intervals(interval_text)

print(count_values(interval_set, value_text))
print(interval_size(interval_set))
