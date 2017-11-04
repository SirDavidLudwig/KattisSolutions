import sys

xOcc = 0
yOcc = 0
x1, y1 = list(map(int, sys.stdin.readline().split()))
x2 = y2 = -1
for i in range(2):
	point = list(map(int, sys.stdin.readline().split()))
	if point[0] == x1:
		xOcc = 1
	else:
		x2 = point[0]
	if point[1] == y1:
		yOcc = 1
	else:
		y2 = point[1]

print(x2 if xOcc == 1 else x1, y2 if yOcc == 1 else y1)
