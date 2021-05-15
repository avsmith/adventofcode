#!/usr/bin/env python


def get_fill_pos(row, col):
    length = row + col - 1
    start = length * (length - 1) // 2
    return start + col


def get_answer(x, mult, div, row, col):
    for i in range(get_fill_pos(row, col) - 1):
        x = (x * mult) % div
    return x


print("Part 1:", get_answer(20151125, 252533, 33554393, 2981, 3075))
