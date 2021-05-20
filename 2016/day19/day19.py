#!/usr/bin/env python

input = 3014603


def seed_elves(num):
    start = dict()
    for i in range(num):
        start[i + 1] = 1
    return start


def find_elf(num, part2=False):
    elves = seed_elves(num)
    presents = [k for k in elves if elves[k] > 0]
    while len(presents) > 1:
        for i in range(len(presents)):
            if elves[presents[i]] > 0:
                if not part2:
                    if i == len(presents) - 1:
                        target = presents[0]
                    else:
                        target = presents[i + 1]
                    elves[presents[i]] += elves[target]
                    elves[target] = 0
                else:
                    remaining = [k for k in elves if elves[k] > 0]
                    if len(remaining) % 1000 == 0 or len(remaining) < 10 == 0:
                        print(len(remaining))
                    if len(remaining) > 1:
                        target = find_across(remaining, presents[i])
                        elves[presents[i]] += elves[target]
                        elves[target] = 0

        presents = [k for k in elves if elves[k] > 0]
    return presents[0]


def find_across(list, elf):
    across = list.index(elf) + len(list) // 2
    if across >= len(list):
        across = across - len(list)
    return list[across]


# print("Part 1:", find_elf(input))
print("Part 2:", find_elf(input, True))
