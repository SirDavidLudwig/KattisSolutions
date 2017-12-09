from math import ceil, sqrt

for i in range(int(input())):
	totalScore = 0
	for j in range(int(input())):
		point = tuple(map(int, input().split()))
		p = max(1, ceil(sqrt(point[0]**2 + point[1]**2)/20))
		if p < 11:
			totalScore += (11-p)
	print(totalScore)
