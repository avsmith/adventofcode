#!/usr/bin/env python

fac1 = 16807
fac2 = 48271

num1 = 591
num2 = 393


limit = 2147483647

count = 0

for i in range(40 * 10**6):
    num1 = (fac1 * num1) % limit
    num2 = (fac2 * num2) % limit
    if (num1 % 2**16) == (num2 % 2**16):
        count += 1

print("Star 1: {}".format(count))

count2 = 0
checked = 0


def gencalc(num, fac, limit):
    num = (fac * num) % limit
    return num


def generator(num, fac, limit, divisor):
    num = gencalc(num, fac, limit)
    while num % divisor != 0:
        num = gencalc(num, fac, limit)
    return num


num1 = 591
num2 = 393

while checked < 5 * 10**6:
    num1 = generator(num1, fac1, limit, 4)
    num2 = generator(num2, fac2, limit, 8)
    checked += 1
    if (num1 % 2**16) == (num2 % 2**16):
        count2 += 1

print("Star 2: {}".format(count2))
