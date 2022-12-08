#!/usr/bin/env python

import os
import sys

f = open(os.path.join(sys.path[0], "input07.txt"))
input = f.read()


class Dir:
    def __init__(self, name, parent=None, part2=False):
        self.name = name
        self.part2 = part2
        self.subdirs = list()
        self.files = list()
        self.parent = parent

    #        self.path = ""
    #        if parent == None:
    #            self.path = name
    #        else:
    #            par = next((x for x in dirs if x.name == parent), None)
    #            print("Par", par.name)
    #            self.path += par.path + name + "/"

    def addfile(self, size, name):
        self.files.append(File(size, name))

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
    print(" ", "Name", dir.name, "Parent", dir.parent, "Subs", dir.subdirs)
    for f in dir.files:
        print(" F", f.name, f.size)
    for c in dir.subdirs:
        print(" D", c)


dirs = list()

for line in test.splitlines():
    #    print("\nLine", line)
    items = line.split()
    if len(items) == 3:
        #        print("Line", line)
        if (items[2]) == "/":
            curdir = Dir(items[2])
            dirs.append(curdir)
        else:
            if items[2] == "..":
                parent = curdir.parent
                if parent is not None:
                    curdir = next((x for x in dirs if x.name == parent), None)
            else:
                curdir = next((x for x in dirs if x.name == items[2]), None)
    elif items[0] == "dir":
        dirs.append(Dir(items[1], curdir.name))
        curdir.addchild(items[1])

    elif items[0].isnumeric():
        curdir.addfile(int(items[0]), items[1])
#    describe(curdir)


def calcsize(dir):
    size = 0
    for f in dir.files:
        size += f.size
    for s in dir.subdirs:
        d = next((x for x in dirs if x.name == s), None)
        size += calcsize(d)
    #    print(dir.name, dir.subdirs, size)
    return size


totalsize = 0
for d in dirs:
    #    describe(d)
    dirsize = calcsize(d)
    if dirsize <= 100000:
        #        print("ADD")
        totalsize += dirsize
#    print(d.name, dirsize, "\n")

print(totalsize)
