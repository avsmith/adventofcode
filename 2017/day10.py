#!/usr/bin/env python

testseq = [3, 4, 1, 5]
sequence = [157, 222, 1, 2, 177, 254, 0, 228, 159, 140, 249, 187, 255, 51, 76, 30]


def intseq(x):
    return [i for i in range(x)]


def subrev(x, n, pos):
    if n + pos > len(x):
        toreverse = x[pos:] + x[: n - (len(x) - pos)]
        reversed = toreverse[::-1]
        x = (
            reversed[len(x) - pos :]
            + x[n - (len(x) - pos) : pos]
            + reversed[: len(x) - pos]
        )
    else:
        x = x[:pos] + x[pos : pos + n :][::-1] + x[pos + n :]
    return x


def checksum(x):
    return x[0] * x[1]


def makeinput(x, seqadd=[17, 31, 73, 47, 23]):
    x = [ord(i) for i in list(x)] + seqadd
    return x


def compacthash(x):
    res = 0
    for i in x:
        res ^= i
    return res


def sparsehash(x, d=intseq(256)):
    curs = 0
    rnd = 0
    for i in range(64):
        for j in range(len(x)):
            length = int(x[j])
            skip = length + rnd
            rnd += 1
            d = subrev(d, length, curs)
            curs = (skip + curs) % len(d)
    h = ""
    step = 16
    for i in range(0, len(d), step):
        subd = d[i : i + step]
        ch = compacthash(subd)
        h = h + hexstring(ch)
    return h


data = intseq(256)
cursor = 0

for i in range(len(sequence)):
    length = int(sequence[i])
    skip = length + i
    data = subrev(data, length, cursor)
    cursor = (skip + cursor) % len(data)


def hexstring(x):
    return "{:02x}".format(x)


print("Star 1 checksum: {}".format(checksum(data)))

input = makeinput(",".join([str(i) for i in sequence]))

print("Star 2 checksum: {}".format(sparsehash(input)))
