#!/usr/bin/env python

from itertools import product
from collections import defaultdict
import numpy as np

target = 100
n = 4


class Ingredient:
    def __init__(self, name, capacity, durability, flavor, texture, calories):
        self.name = name
        self.capacity = int(capacity)
        self.durability = int(durability)
        self.flavor = int(flavor)
        self.texture = int(texture)
        self.calories = int(calories)

    def __getitem__(self, item):
        return getattr(self, item)

    def __repr__(self):
        return f"{self.name} {self.capacity} {self.durability} {self.flavor} {self.texture} {self.calories}"


testdata = """Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3
"""

data = """Sprinkles: capacity 2, durability 0, flavor -2, texture 0, calories 3
Butterscotch: capacity 0, durability 5, flavor -3, texture 0, calories 3
Chocolate: capacity 0, durability 0, flavor 5, texture -1, calories 8
Candy: capacity 0, durability -1, flavor 0, texture 5, calories 8
"""


ingredients = list()


def amt_totals(target, n):
    numbers = list(range(1, target))
    totals = [x for x in product(numbers, repeat=n) if sum(x) == target]
    return totals


for line in data.splitlines():
    items = line.replace(":", "").replace(",", "").split()
    ingred = Ingredient(items[0], items[2], items[4], items[6], items[8], items[10])
    ingredients.append(ingred)

properties = ["capacity", "durability", "flavor", "texture"]


def find_recipe(ingredients, diet=None, target=100):
    best = None
    amounts = amt_totals(target, len(ingredients))
    for recipe in sorted(amounts):
        totals = defaultdict(int)
        calories = 0
        for i in range(len(recipe)):
            calories += ingredients[i]["calories"] * recipe[i]
            for prop in properties:
                totals[prop] += ingredients[i][prop] * recipe[i]
        if diet is not None and diet != calories:
            continue
        values = [value for value in totals.values()]
        if all(v > 0 for v in values):
            product = np.product(values)
            if best is None or product > best:
                best = product
    return best


print("Part 1:", find_recipe(ingredients))
print("Part 2:", find_recipe(ingredients, diet=500))
