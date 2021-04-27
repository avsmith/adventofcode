#!/usr/bin/env python

import re

A_LOWERCASE = ord("a")
ALPHABET_SIZE = 26


def _decompose(number):
    while number:
        number, remainder = divmod(number - 1, ALPHABET_SIZE)
        yield remainder


def base_10_to_alphabet(number):
    return "".join(chr(A_LOWERCASE + part) for part in _decompose(number))[::-1]


def base_alphabet_to_10(letters):
    return sum(
        (ord(letter) - A_LOWERCASE + 1) * ALPHABET_SIZE ** i
        for i, letter in enumerate(reversed(letters.lower()))
    )


def increment_string(string):
    inc_string = base_10_to_alphabet(base_alphabet_to_10(string) + 1)
    return inc_string


def test_consecutive_chars(string, number=3):
    for i in range(len(string) - number + 1):
        substring = string[i : (i + number)]
        if (
            ord(substring[0]) == ord(substring[1]) - 1
            and ord(substring[0]) == ord(substring[2]) - 2
        ):
            return True
    return False


def test_good_characters(string, illegal="ilo"):
    if len(set(string) - set(illegal)) == len(set(string)):
        return True
    return False


def test_consecutive_pairs(string):
    splitstring = [iters.group(0) for iters in re.finditer(r"(\D)\1*", string)]
    doublestrings = [s for s in splitstring if len(s) > 1]
    if len(set(doublestrings)) > 1:
        return True
    return False


def next_password(string):
    for i in range(
        base_alphabet_to_10(string) + 1,
        int((ALPHABET_SIZE ** (len(string) + 1) - 1) / (ALPHABET_SIZE - 1)),
    ):
        possible_password = base_10_to_alphabet(i)
        if (
            test_consecutive_chars(possible_password)
            and test_good_characters(possible_password)
            and test_consecutive_pairs(possible_password)
        ):
            return possible_password
    else:
        return "ERROR"


input = "cqjxjnds"

print("Part 1:", next_password(input))
