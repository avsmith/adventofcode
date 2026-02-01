#!/usr/bin/env python3

from pathlib import Path

test = """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.
"""
text = Path("input04.txt").read_text()

mat = [
    [1 if c == "@" else 0 for c in line.strip()] for line in text.strip().splitlines()
]


def stacked_pallets(matrix, row, col):
    pallets = 0
    neighbors_list = []
    # Define possible neighbor offsets: (delta_row, delta_col)
    neighbors = [(1, 1), (1, 0), (1, -1), (0, 1), (0, -1), (-1, 1), (-1, 0), (-1, -1)]

    # Get matrix dimensions
    num_rows = len(matrix)
    num_cols = len(matrix[0]) if num_rows > 0 else 0
    for dr, dc in neighbors:
        new_row, new_col = row + dr, col + dc
        if 0 <= new_row < num_rows and 0 <= new_col < num_cols:
            if matrix[new_row][new_col] == 1:
                pallets += 1
    if pallets < 4:
        return True
    return False


accessable = 0
for i, row in enumerate(mat):
    for j, value in enumerate(row):
        if mat[i][j] == 1:
            accessable += stacked_pallets(mat, i, j)

print(accessable)