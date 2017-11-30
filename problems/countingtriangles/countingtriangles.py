from itertools import combinations
import sys

memoIntersections = {}

def lineIntersection(line1, line2):
	try:
		return memoIntersections[tuple(set([line1, line2]))]
	except KeyError:
		pass

	xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
	ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

	def det(a, b):
		return a[0] * b[1] - a[1] * b[0]

	div = det(xdiff, ydiff)
	if div == 0:
		return None

	d = (det(*line1), det(*line2))
	x = det(d, xdiff) / div
	y = det(d, ydiff) / div

	xMin = max(min(line1[0][0], line1[1][0]), min(line2[0][0], line2[1][0]))
	xMax = min(max(line1[0][0], line1[1][0]), max(line2[0][0], line2[1][0]))
	yMin = max(min(line1[0][1], line1[1][1]), min(line2[0][1], line2[1][1]))
	yMax = min(max(line1[0][1], line1[1][1]), max(line2[0][1], line2[1][1]))

	memoIntersections[tuple(set([line1, line2]))] = xMin < x < xMax and yMin < y < yMax

	return memoIntersections[tuple(set([line1, line2]))]


n = int(input())
while n != 0:
	lines = []
	intersections = {}
	for i in range(n):
		line = tuple(map(float, input().split()))
		lines.append((line[0:2], line[2:]))
	for pair in combinations(lines, 2):
		if lineIntersection(pair[0], pair[1]):
			try:
				intersections[pair[0]].append(pair[1])
			except KeyError:
				intersections[pair[0]] = [pair[1]]

	triangles = 0
	for line in lines:
		if line in intersections and len(intersections[line]) > 1:
			for pair in combinations(intersections[line], 2):
				if lineIntersection(pair[0], pair[1]):
					triangles += 1
	print(triangles)

	n = int(input())
