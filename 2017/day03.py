#!/usr/bin/env python

from math import ceil, sqrt

seed = 325489

def dist_row(x):
	return(ceil((sqrt(x)-1)/2))

print("\n\n==== Star 1 ====")

print("Answer dist_row: {}".format(dist_row(seed)))

def end_ring(x):
	return((2*x+1)**2)

print("Answer end_ring: {}".format(end_ring(seed)))	
	
def dist_ring(x):
	return(abs((end_ring(dist_row(x))-x) % (dist_row(x)*2)- dist_row(x)))

print("Answer dist_ring: {}".format(dist_ring(seed)))

def dist_man(x):
	return(dist_row(x)+dist_ring(x))

print("Answer star #1 {}".format(dist_man(seed)))

print("\n\n==== Star 2 ====")

