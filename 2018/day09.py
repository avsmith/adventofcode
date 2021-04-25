#!/usr/bin/env python

from collections import deque
import sys


def marble_mania(n_marbles, n_players):
    marbles = deque([0])
    scores = [0] * n_players
    for i in range(1, n_marbles + 1):
        if i % 23 != 0:
            marbles.append(i)
            marbles.rotate(-1)
        else:
            cur_player = i % n_players
            scores[cur_player] += i
            marbles.rotate(8)
            scores[cur_player] += marbles.pop()
            marbles.rotate(-2)
    return max(scores)


print(marble_mania(70784, 452))
print(marble_mania(70784 * 100, 452))
