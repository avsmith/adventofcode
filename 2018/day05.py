#!/usr/bin/env python

from string import ascii_lowercase

f = open("day05.txt", "r")
string = f.read().rstrip()


def adjreplace(word):
    newword = None
    while newword != word:
        newword = word
        for c in ascii_lowercase:
            word = word.replace(c + c.upper(), "")
            word = word.replace(c.upper() + c, "")
    return word


print(len(adjreplace(string)))

smallest = len(string)
for c in ascii_lowercase:
    ns = string
    ns = ns.replace(c, "")
    ns = ns.replace(c.upper(), "")
    ns_len = len(adjreplace(ns))
    if ns_len < smallest:
        smallest = ns_len

print(smallest)
