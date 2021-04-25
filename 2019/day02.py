#!/usr/bin/env python


def convert_input(day02):
    l = day02.strip().split(",")
    c = [int(i) for i in l]
    return c


data = "1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,13,1,19,1,10,19,23,1,23,9,27,1,5,27,31,2,31,13,35,1,35,5,39,1,39,5,43,2,13,43,47,2,47,10,51,1,51,6,55,2,55,9,59,1,59,5,63,1,63,13,67,2,67,6,71,1,71,5,75,1,75,5,79,1,79,9,83,1,10,83,87,1,87,10,91,1,91,9,95,1,10,95,99,1,10,99,103,2,103,10,107,1,107,9,111,2,6,111,115,1,5,115,119,2,119,13,123,1,6,123,127,2,9,127,131,1,131,5,135,1,135,13,139,1,139,10,143,1,2,143,147,1,147,10,0,99,2,0,14,0"


def intcode(d, r1=None, r2=None):
    l = convert_input(d)
    pos = 0
    if r1 is not None:
        l[1] = r1
    if r2 is not None:
        l[2] = r2
    while l[pos] != 99:
        tt = l[pos]
        i1 = l[l[pos + 1]]
        i2 = l[l[pos + 2]]
        recip = l[pos + 3]
        #    print(pos, tt, i1, i2, recip)
        if tt == 1:
            l[recip] = i1 + i2
        elif tt == 2:
            l[recip] = i1 * i2
        else:
            print(tt, i1, i2, recip)
            print("ERROR")
            break
        pos = pos + 4
    return l[0]


def intcode_target(numbers, target):
    for r1 in range(100):
        for r2 in range(100):
            if intcode(numbers, r1, r2) == target:
                return 100 * r1 + r2


# print(intcode(convert_input('1,0,0,0,99')))
# print(intcode(convert_input('2,3,0,3,99')))
# print(intcode(convert_input('2,4,4,5,99,0')))
# print(intcode(convert_input('1,1,1,4,99,5,6,0,99')))
print(intcode(data, r1=12, r2=2))
print(intcode_target(data, 19690720))
