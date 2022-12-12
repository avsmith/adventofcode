#!/usr/bin/env python

import os
import sys

from collections import deque

f = open(os.path.join(sys.path[0], "input21.txt"))
input = f.read()

password = "abcdefgh"

password = deque([x for x in password])

for line in input.splitlines():
    items = line.split()
    if items[0] == "swap":
        if items[1] == "position":
            a = int(items[2])
            b = int(items[5])
        elif items[1] == "letter":
            a = password.index(items[2])
            b = password.index(items[5])
        password[a], password[b] = password[b], password[a]
    elif items[0] == "rotate":
        if items[1] == "right":
            rot = int(items[2])
        elif items[1] == "left":
            rot = -int(items[2])
        elif items[1] == "based":
            idx = password.index(items[-1])
            if idx >= 4:
                rot = 2 + idx
            else:
                rot = 1 + idx
        password.rotate(rot)
    elif items[0] == "reverse":
        a = int(items[2])
        b = int(items[4])
        if a > 0 and b < len(password) - 1:
            temp = list(password)
            password = deque(temp[:a] + temp[b : a - 1 : -1] + temp[b + 1 :])
        elif a > 0 and b == len(password) - 1:
            temp = list(password)
            password = deque(temp[:a] + temp[b : a - 1 : -1])
        elif a == 0 and b < len(password) - 1:
            temp = list(password)
            password = deque(temp[b::-1] + temp[b + 1 :])
        elif a == 0 and b == len(password) - 1:
            password.reverse()
    elif items[0] == "move":
        let = password[int(items[2])]
        password.remove(let)
        b = int(items[5])
        password.insert(b, let)

print("".join(password))
print("")
