import sys

data = tuple(map(float, sys.stdin.readline().split()))
while data[0] != 0:
	x1, y1, x2, y2, p = data
	print((abs(x1 - x2)**p + abs(y1 - y2)**p)**(1/p))
	data = tuple(map(float, sys.stdin.readline().split()))
