#!/usr/bin/env python

import numpy as np


dirs = [1, -1, -1j, 1j]
cars_map = [">", "<", "^", "v"]
car_to_dir = dict(zip(cars_map, dirs))
dir_to_car = {v: k for k, v in car_to_dir.items()}

turns = ["/", "\\"]
trans = [1, -1]

turn_convert = dict(zip(turns, trans))


def draw_car(car):
    x = int(car["pos"].real)
    y = int(car["pos"].imag)
    d = car["dir"]
    c = dir_to_car[d]
    return ([x, y], c)


def get_map(r, carlist):
    xmax = int(max(np.real(list(r.keys()))))
    ymax = int(max(np.imag(list(r.keys()))))
    g = [[" "] * (ymax + 1) for i in range(xmax + 1)]
    for k, v in road.items():
        g[int(k.real)][int(k.imag)] = v
        for c in carlist:
            cp, car = draw_car(c)
            g[cp[0]][cp[1]] = car
    return "\n".join(["".join(a) for a in zip(*g)])


def car_positions(cars):
    positions = []
    for i in range(len(cars)):
        position = cars[i]["pos"]
        positions.append(position)
    return positions


def remove_cars(cars, crash_positions):
    remaining_cars = []
    for i in range(len(cars)):
        if cars[i]["pos"] not in crash_positions:
            remaining_cars.append(cars[i])
    return remaining_cars


lines = open("day13.txt").read().splitlines()

road = {
    x + 1j * y: v
    for y, line in enumerate(lines)
    for x, v in enumerate(line)
    if v.strip()
}
carpos = [key for (key, value) in road.items() if value in [">", "^", "<", "v"]]

cars = []
for p in carpos:
    if road[p] in cars_map:
        direction = car_to_dir[road[p]]
    road[p] = "|" if np.iscomplex(direction) else "-"
    cars.append({"dir": direction, "pos": p, "turn": 0})


crash = False
print(len(cars))

while len(cars) > 1:
    crash_positions = []
    cars = sorted(cars, key=lambda k: (k["pos"].imag, k["pos"].real))
    for i in range(len(cars)):
        position = cars[i]["pos"]
        direction = cars[i]["dir"]

        r = road[position]
        mult = 1
        if r == "+":
            if cars[i]["turn"] % 3 == 0:
                mult = -1j
            elif cars[i]["turn"] % 3 == 2:
                mult = 1j
            cars[i]["turn"] += 1
        if r in ["/", "\\"]:
            mult = turn_convert[r] * (1 if np.iscomplex(direction) else -1) * 1j
        direction *= mult
        position += direction
        cars[i]["pos"] = position
        cars[i]["dir"] = direction
        #    other_cars = [x for j,x in enumerate(cars) if j!=i]
        if any(
            c in [position, position - direction]
            for c in car_positions([x for j, x in enumerate(cars) if j != i])
        ):
            crash = True
            crash_positions.append(position)
            print(crash_positions)
    uncrashed = remove_cars(cars, crash_positions)
    cars = uncrashed

print(cars)
"""    if road[pos] == '+':
        direction = next(d for d in [direction*1j, direction*-1j]
                         if pos+d in road and d != path[-1]-pos)
    path += [pos]
    pos += direction
print(''.join(c for c in map(road.get, path) if c.isalpha()))
print(len(path))"""
