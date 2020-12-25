#!/usr/bin/env python

import re
import os, sys
from collections import defaultdict

movere = re.compile(r'(e|se|sw|w|nw|ne)')

input = '''sesenwnenenewseeswwswswwnenewsewsw
neeenesenwnwwswnenewnwwsewnenwseswesw
seswneswswsenwwnwse
nwnwneseeswswnenewneswwnewseswneseene
swweswneswnenwsewnwneneseenw
eesenwseswswnenwswnwnwsewwnwsene
sewnenenenesenwsewnenwwwse
wenwwweseeeweswwwnwwe
wsweesenenewnwwnwsenewsenwwsesesenwne
neeswseenwwswnwswswnw
nenwswwsewswnenenewsenwsenwnesesenew
enewnwewneswsewnwswenweswnenwsenwsw
sweneswneswneneenwnewenewwneswswnese
swwesenesewenwneswnwwneseswwne
enesenwswwswneneswsenwnewswseenwsese
wnwnesenesenenwwnenwsewesewsesesew
nenewswnwewswnenesenwnesewesw
eneswnwswnwsenenwnwnwwseeswneewsenese
neswnwewnwnwseenwseesewsenwsweewe
wseweeenwnesenwwwswnew
'''

f = open(os.path.join(sys.path[0], 'input24.txt'))
input = f.read()


#e, se, sw, w, nw, and ne
turned = defaultdict(lambda:1)

for line in input.splitlines():
  pos = 0+0j
  moves = movere.findall(line)
  for move in moves:
    if move == 'e':
      pos += 1
    elif move == 'se':
      pos += 1-1j
    elif move == 'sw':
      pos += 0-1j
    elif move == 'w':
      pos += -1
    elif move == 'nw':
      pos += -1+1j
    elif move == 'ne':
      pos += 1j
  turned[pos] *= -1

print(abs(sum([x for x in turned.values() if x == -1 ])))

print(turned[100+100j])
