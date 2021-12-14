#!/usr/bin/env python

test = """NNBC

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C
"""

input = """ONHOOSCKBSVHBNKFKSBK

HO -> B
KB -> O
PV -> B
BV -> C
HK -> N
FK -> H
NV -> C
PF -> K
FV -> B
NH -> P
CO -> N
HV -> P
OH -> H
BC -> H
SP -> C
OK -> F
KH -> N
HB -> V
FP -> N
KP -> O
FB -> O
FH -> F
CN -> K
BP -> P
SF -> O
CK -> K
KN -> O
VK -> C
HP -> N
KK -> V
KO -> C
OO -> P
BH -> B
OC -> O
HC -> V
HS -> O
SH -> V
SO -> C
FS -> N
CH -> O
PC -> O
FC -> S
VO -> H
NS -> H
PH -> C
SS -> F
BN -> B
BF -> F
NC -> F
CS -> F
NN -> O
FF -> P
OF -> H
NF -> O
SC -> F
KC -> F
CP -> H
CF -> K
BS -> S
HN -> K
CB -> P
PB -> V
VP -> C
OS -> C
FN -> B
NB -> V
BB -> C
BK -> V
VF -> V
VC -> O
NO -> K
KF -> P
FO -> C
OB -> K
ON -> S
BO -> V
KV -> H
CC -> O
HF -> N
VS -> S
PN -> P
SK -> F
PO -> V
HH -> F
VV -> N
VH -> N
SV -> S
CV -> B
KS -> K
PS -> V
OV -> S
SB -> V
NP -> K
SN -> C
NK -> O
PK -> F
VN -> P
PP -> K
VB -> C
OP -> P
"""

move, translation = input.split("\n\n")


translate = {}

for t in translation.splitlines():
    ref, out = t.split(" -> ")
    translate[ref] = out

overall = []
for _ in range(10):
    insertion = []
    for i in range(len(move) - 1):
        insertion += translate[move[i : i + 2]]

    newmove = ""
    for i in range(len(insertion)):
        newmove = newmove + move[i] + insertion[i]

    newmove += move[-1]
    move = newmove

    counts = []
    for c in set(move):
        counts.append(move.count(c))

    counts = sorted(counts)


print("Part 1:", counts[-1] - counts[0])

# key = ''.join(translate.keys())
# for c in sorted(move):
# 	print(c, key.count(c))
