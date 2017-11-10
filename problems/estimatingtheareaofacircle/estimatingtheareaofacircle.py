from math import pi
import sys

r, m, c = map(float, sys.stdin.readline().split())

while r != 0 and m != 0 and c != 0:
	print(pi*r**2, c/m*r**2*4)
	r, m, c = map(float, sys.stdin.readline().split())
