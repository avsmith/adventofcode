#!/usr/bin/env python

import os
import sys

f = open(os.path.join(sys.path[0], "input07.txt"))
input = f.read()


class Dir:
    def __init__(self, name, path=None, part2=False):
        if path is None:
            self.path = "/"
        elif path == "/":
            self.path = path + name
        else:
            self.path = path + "/" + name
        self.part2 = part2
        self.subdirs = list()
        self.files = list()

    def addfile(self, size, path):
        self.files.append(File(size, path))

    def addchild(self, child):
        self.subdirs.append(child)


class File:
    def __init__(self, size, name):
        self.size = size
        self.name = name


test = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
"""


def describe(dir):
    print(" Path", dir.path)
    for f in dir.files:
        print(" F", f.name, f.size)
    for c in dir.subdirs:
        print(" D", c.path)


dirs = list()

for line in input.splitlines():
    items = line.split()
    if len(items) == 3:
        if (items[2]) == "/":
            curdir = Dir(items[2])
            dirs.append(curdir)
            path = "/"
        else:
            if items[2] == "..":
                splitpath = path.split("/")
                path = "/".join(splitpath[:-1])
                if path == "":
                    path = "/"
                curdir = next((x for x in dirs if x.path == path), None)
            else:
                if path == "/":
                    path = path + items[2]
                else:
                    path = path + "/" + items[2]
                curdir = next((x for x in dirs if x.path == path), None)
    elif items[0] == "dir":
        newdir = Dir(items[1], curdir.path)
        dirs.append(newdir)
        curdir.addchild(newdir)
    elif items[0].isnumeric():
        curdir.addfile(int(items[0]), items[1])
#    describe(curdir)


def calcsize(dir):
    size = 0
    for f in dir.files:
        size += f.size
    for s in dir.subdirs:
        d = next((x for x in dirs if x.path == s.path), None)
        size += calcsize(d)
    return size


totalsize = 0

# btgrv
# d = next((x for x in dirs if x.name == "ddhfvv"), None)
# print(d.name, d.subdirs)

for d in dirs:
    #    for s in d.subdirs:
    #        print(s)
    #    describe(d)
    dirsize = calcsize(d)
    if dirsize <= 100000:
        #        print("ADD")
        totalsize += dirsize
#    print(d.name, dirsize, "\n")

print(totalsize)
