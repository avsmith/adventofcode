#!/usr/bin/env python3
import math
from pathlib import Path


def score(nums: list[int], op: str) -> int:
	"""Apply op to nums."""
	return math.prod(nums) if op == "*" else sum(nums)


def parse_token_matrix(lines: list[str]):
	"""Part 1 parsing: whitespace tokens; digits -> int; ops stay str."""
	return [
		[int(tok) if tok.isdigit() else tok for tok in line.split()]
		for line in lines
	]


def part1(lines: list[str]) -> int:
	matrix = parse_token_matrix(lines)
	# each column is [n1, n2, ..., op]
	return sum(score(list(col[:-1]), col[-1]) for col in zip(*matrix))


def part2(lines: list[str]) -> int:
	"""
	Part 2 parsing is fixed-width character based.

	We:
	  1) find operator positions on the last line
	  2) for each operator, scan character columns in its block right-to-left
	  3) read digits vertically in that character column (blanks => 0)
	  4) apply op across those numbers and sum
	"""
	op_line = lines[-1]
	width = len(op_line)

	digit_rows = lines[:-1]

	op_positions = [i for i, c in enumerate(op_line) if c in "*+"]
	op_positions.append(width + 1)

	total = 0
	for k in range(len(op_positions) - 1):
		op_pos = op_positions[k]
		next_pos = op_positions[k + 1]
		op = op_line[op_pos]

		cols = range(next_pos - 2, op_pos - 1, -1)

		nums = []
		for col in cols:
			s = "".join(r[col] for r in digit_rows)
			nums.append(int(s))

		total += score(nums, op)

	return total


def main():
	text = Path("input06.txt").read_text()
	lines = text.splitlines()

	print("Part1:", part1(lines))
	print("Part2:", part2(lines))


if __name__ == "__main__":
	main()
	