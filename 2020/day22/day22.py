#!/usr/bin/env python

input = '''Player 1:
18
50
9
4
25
37
39
40
29
6
41
28
3
11
31
8
1
38
33
30
42
15
26
36
43

Player 2:
32
44
19
47
12
48
14
2
13
10
35
45
34
7
5
17
46
21
24
49
16
22
20
27
23
'''

testinput = '''Player 1:
9
2
6
3
1

Player 2:
5
8
4
7
10
'''

from collections import deque
import copy

def card_game(crds1, crds2, recurs = False):
  cset1 = copy.copy(crds1)
  cset2 = copy.copy(crds2)
  while len(cset1) > 0 and len(cset2) > 0:
    c1 = cset1.popleft()
    c2 = cset2.popleft()
    if c1 > c2:
      cset1.extend([c1,c2])
    elif c2 > c1:
      cset2.extend([c2,c1])
  if len(cset1) > len(cset2):
    return(calc_score(cset1))
  else:
    return(calc_score(cset2))

def calc_score(dq):
  tot = 0
  dq.reverse()
  for i in range(len(dq)):
    tot += dq[i]*(i+1)
  return(tot)

(player1, player2) = input.split("\n\n")

cards1 = deque([int(x) for x in player1.splitlines()[1:]])
cards2 = deque([int(x) for x in player2.splitlines()[1:]])

print(card_game(cards1, cards2))

