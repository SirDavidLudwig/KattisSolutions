from math import *
import sys

for i in range(int(sys.stdin.readline())):
	v0, angle, x, h1, h2 = tuple(map(float, sys.stdin.readline().split(" ")))
	t = x/(v0*cos(radians(angle)))
	y = v0 * t * sin(radians(angle)) - 0.5*9.81*t**2
	print("Safe" if h1+1 < y < h2-1 else "Not Safe")
