#!/usr/bin/env python

import numpy as np

input = """Player 1 starting position: 7
Player 2 starting position: 6
"""

positions = np.array([], dtype="i")


def playgame(pos):
    scores = np.array([0, 0], dtype="i")
    nextroll = np.array([0, 1, 2], dtype="i")
    rolls = 0
    player = 0
    while all(scores < 1000):
        curplayer = player % 2
        delta = sum((nextroll + 3 * rolls) % 100 + 1)
        if (pos[curplayer] + delta) % 10 == 0:
            newpos = 10
        else:
            newpos = (pos[curplayer] + delta) % 10
        pos[curplayer] = newpos
        scores[curplayer] += pos[curplayer]

        rolls += 1

        #        print(rolls, player, delta, newpos,pos,  scores)
        player += 1
        if any(scores >= 1000):
            return min(scores) * rolls * 3


for line in input.splitlines():
    positions = np.append(positions, [int(line[-1])])


print("Part 1:", playgame(positions))
