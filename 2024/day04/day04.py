#!/usr/bin/env python

import os
import sys
import collections

f = open(os.path.join(sys.path[0], "input04.txt"))
input = f.read()

# Based heavily on https://zhaqenl.github.io/en/wordsearch/
# I did work out the extension to cover part2

def matrixify(grid, separator="\n"):
    return grid.split(separator)


def coord_char(coord, matrix):
    row_index, column_index = coord
    return matrix[row_index][column_index]


def convert_to_word(coord_matrix, matrix):
    return "".join([coord_char(coord, matrix) for coord in coord_matrix])


def find_base_match(char, matrix):
    base_matches = [
        (row_index, column_index)
        for row_index, row in enumerate(matrix)
        for column_index, column in enumerate(row)
        if char == column
    ]

    return base_matches


def matched_neighbors(coord, char, matrix, row_length, col_length):
    row_num, col_num = coord
    neighbors_coords = [
        (row, column)
        for row in range(row_num - 1, row_num + 2)
        for column in range(col_num - 1, col_num + 2)
        if row_length > row >= 0
        and col_length > column >= 0
        and coord_char((row, column), matrix) == char
        and not (row, column) == coord
    ]

    return neighbors_coords


def complete_line(base_coord, targ_coord, word_len, row_length, col_len):
    if word_len == 2:
        return base_coord, targ_coord

    line = [base_coord, targ_coord]
    diff_1 = targ_coord[0] - base_coord[0]
    diff_2 = targ_coord[1] - base_coord[1]

    for _ in range(word_len - 2):
        line += [(line[-1][0] + diff_1, line[-1][1] + diff_2)]

    if 0 <= line[-1][0] < row_length and 0 <= line[-1][1] < col_len:
        return line
    return []


def complete_match(word, matrix, base_match, word_len, row_len, col_len):
    new = (
        complete_line(base, n, word_len, row_len, col_len)
        for base in base_match
        for n in matched_neighbors(base, word[1], matrix, row_len, col_len)
    )
    return [ero for ero in new if convert_to_word(ero, matrix) == word]


def find_matches(word, grid, separator="\n"):
    word_len = len(word)
    matrix = matrixify(grid, separator)
    row_len, column_len = len(matrix), len(matrix[0])
    base_matches = find_base_match(word[0], matrix)

    if column_len < word_len > row_len or not base_matches:
        return []
    elif word_len == 1:
        return base_matches

    return complete_match(word, matrix, base_matches, word_len, row_len, column_len)


def find_diagonals(matches):
    diags = []
    for m in matches:
        if m[0][0] != m[2][0] and m[0][1] != m[2][1]:
            diags += [m]
    return diags


def count_overlaps(diags):
    middles = [x[1] for x in diags]
    return len(
        [item for item, count in collections.Counter(middles).items() if count > 1]
    )


def part1(word, string_grid, separator="\n"):
    return len(find_matches(word, string_grid, separator))


def part2(word, string_grid, separator="\n"):
    candidates = find_matches(word, string_grid, separator)
    diags = find_diagonals(candidates)
    xcount = count_overlaps(diags)
    return xcount


print(part1("XMAS", input))
print(part2("MAS", input))
