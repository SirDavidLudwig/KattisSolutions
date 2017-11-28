from math import sqrt
import sys

coords = [
	(-1,  1), ( 0,  1), ( 1,  1),
	(-1,  0), ( 0,  0), ( 1,  0),
	(-1, -1), ( 0, -1), ( 1, -1)
]

coordMap = {}
for i in range(3):
	for j, v in enumerate(map(int, input().split())):
		coordMap[v] = coords[3*i+j]

t = 0
c = coordMap[1]
for i in range(2, 10):
	n = coordMap[i]
	t += sqrt((n[0]-c[0])**2+(n[1]-c[1])**2)
	c = n
print("%.6f" % t)
