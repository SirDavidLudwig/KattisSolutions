import math
import sys

n = int(input())

points = []
for i in range(n):
	points.append(tuple(map(float, input().split())))

tour = [0]
used = [False]*n

def dist(a, b):
	return math.sqrt((points[b][0]-points[a][0])**2 + (points[b][1]-points[a][1])**2)

used[0] = True
for i in range(1, n):
	best = -1
	for j in range(n):
		if not used[j] and (best == -1 or dist(tour[i-1], j) < dist(tour[i-1], best)):
			best = j
	tour.append(best)
	used[best] = True

for i in tour:
	print(i)
