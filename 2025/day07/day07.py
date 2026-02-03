#!/usr/bin/env python3

from pathlib import Path


def parse_matrix(lines: list[str]):
    """Part 1 parsing: whitespace tokens; digits -> int; ops stay str."""
    code = {"S": 1, ".": 0, "^": -1}
    return [[code[x] for x in row] for row in lines]


def part1(lines: list[str]) -> int:
    matrix = parse_matrix(lines)
    split_count = 0
    for i, line in enumerate(matrix[:-1]):
        beams = [i for i, c in enumerate(line) if c > 0 ]
        next_blocks = [i for i, c in enumerate(matrix[i + 1]) if c == -1]
        for b in beams:
            if b in next_blocks:
                matrix[i + 1][b - 1] = 1
                matrix[i + 1][b] = -1
                matrix[i + 1][b + 1] = 1
                split_count += 1
            else:
                matrix[i + 1][b] = 1

    return split_count

def part2(lines: list[str]) -> int:
    matrix = parse_matrix(lines)
    counts = matrix[0]
    for i, line in enumerate(matrix[:-1]):
        next_counts = [0]*len(line)
        beams = [i for i, c in enumerate(counts) if c > 0 ]
        next_blocks = [i for i, c in enumerate(matrix[i + 1]) if c == -1]
        for b in beams:
            if b in next_blocks:
                next_counts[b-1] += counts[b]
                next_counts[b+1] += counts[b]
            else:
                next_counts[b]+=counts[b]
        counts=next_counts
    return sum(counts)


def main():
    text = Path("input07.txt").read_text()
    lines = text.splitlines()
    if debug:
        print(lines)
    print("Part1:", part1(lines))
    print("Part2:", part2(lines))


if __name__ == "__main__":
    debug = False
    main()
