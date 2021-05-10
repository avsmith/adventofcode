#!/usr/bin/env python

import re
from itertools import combinations, product
from collections import defaultdict

weights = """Weapons:    Cost  Damage  Armor
Dagger        8     4       0
Shortsword   10     5       0
Warhammer    25     6       0
Longsword    40     7       0
Greataxe     74     8       0

Armor:      Cost  Damage  Armor
Leather      13     0       1
Chainmail    31     0       2
Splintmail   53     0       3
Bandedmail   75     0       4
Platemail   102     0       5

Rings:      Cost  Damage  Armor
Damage +1    25     1       0
Damage +2    50     2       0
Damage +3   100     3       0
Defense +1   20     0       1
Defense +2   40     0       2
Defense +3   80     0       3
"""


class Item:
    def __init__(self, name, cost, damage, armor):
        self.name = name
        self.cost = int(cost)
        self.damage = int(damage)
        self.armor = int(armor)

    def __getitem__(self, item):
        return getattr(self, item)

    def __repr__(self):
        return f"{self.name} {self.cost} {self.damage} {self.armor}"


class Fighter(Item):
    def __init__(self, name, cost, damage, armor, points=100):
        super().__init__(name, cost, damage, armor)
        self.points = int(points)
        self.alive = True

    def dead(self):
        ~self.alive


weapons = list()
armors = list()
rings = list()

type = None

for line in weights.splitlines():
    (items) = re.split("  +", line)
    if items[0]:
        if items[0][-1] == ":":
            type = items[0][0:-1]
            continue
        if type == "Weapons":
            weapons.append(Item(items[0], items[1], items[2], items[3]))
        elif type == "Armor":
            armors.append(Item(items[0], items[1], items[2], items[3]))
        elif type == "Rings":
            rings.append(Item(items[0], items[1], items[2], items[3]))

armors.append(Item("None", 0, 0, 0))
rings.append(Item("None", 0, 0, 0))
rings.append(Item("None", 0, 0, 0))


seen = defaultdict(int)
fighters = list()

for combo in list(product(weapons, armors, combinations(rings, 2))):
    name = "-".join([combo[0].name, combo[1].name, combo[2][0].name, combo[2][1].name])
    # Hack to avoid duplicate tests
    # Only works because "None" rings always at end
    seen[name] += 1
    if seen[name] > 1:
        continue
    cost = combo[0].cost + combo[1].cost + combo[2][0].cost + combo[2][1].cost
    armor = combo[0].armor + combo[1].armor + combo[2][0].armor + combo[2][1].armor
    damage = combo[0].damage + combo[1].damage + combo[2][0].damage + combo[2][1].damage
    fighters.append(Fighter(name, cost, damage, armor))


def battle(attacker, defender):
    defender.points = defender.points - max(attacker.damage - defender.armor, 1)
    if defender.points <= 0:
        defender.alive = False


def war(player):
    boss = Fighter("Boss", 0, 8, 2, 109)
    round = 1
    while player.alive and boss.alive:
        if round % 2 == 1:
            battle(player, boss)
        else:
            battle(boss, player)
        round += 1


for player in fighters:
    war(player)

fighters.sort(key=lambda x: x.cost)

print("Part 1:", [f for f in fighters if f.alive][0].cost)
print("Part 2:", [f for f in fighters if not f.alive][-1].cost)
