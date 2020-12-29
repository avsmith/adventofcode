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

def card_game(deck1, deck2, part2 = False):
  round = 1
  while len(deck1) > 0 and len(deck2) > 0:
    print(f"\nOuter Round: {round}" , '\nCards1:', deck1, '\nCards2:',deck2)
    winner = find_winner(deck1, deck2, part2)
    card1 = deck1.popleft()
    card2 = deck2.popleft()
    if winner == 1:
      deck1.extend([  card1,card2])
    elif winner == 2:
      deck2.extend([card2,card1])
    round += 1
  return(max(calc_score(cards1),calc_score(cards2)))
  
def find_winner(d1, d2, part2):
  round = 1
  deck1 = copy.copy(d1)
  deck2 = copy.copy(d2)
  while len(d1)> 0 and len(d2) > 0:
    c1=  deck1.popleft()
    c2 = deck2.popleft()
    print(f"\nInner Round: {round}" , '\nCards1:',c1,'*', d1, '\nCards2:', c2,'*', d2)
    if part2 and len(d1) > c1 and len(d2) > c2:
      return(find_winner(deque(list(deck1)[0:c1]), deque(list(deck2)[0:c2]), part2))
    elif c1 > c2:
      deck1.extend([c1,c2])
    elif c2 > c1:
      deck2.extend([c2,c1])
    round += 1
  if len(deck1) > len(deck2):
    return(1)
  elif len(deck)
  raise Exception("Ooops")

def calc_score(dq):
  tot = 0
  dq.reverse()
  for i in range(len(dq)):
    tot += dq[i]*(i+1)
  return(tot)

(player1, player2) = testinput.split("\n\n")

cards1 = deque([int(x) for x in player1.splitlines()[1:]])
cards2 = deque([int(x) for x in player2.splitlines()[1:]])
print()
#print(card_game(cards1, cards2))
cards1 = deque([int(x) for x in player1.splitlines()[1:]])
cards2 = deque([int(x) for x in player2.splitlines()[1:]])
print()
print(card_game(cards1, cards2, True))
