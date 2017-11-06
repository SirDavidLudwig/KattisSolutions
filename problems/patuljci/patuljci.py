import itertools
import sys

values = [int(sys.stdin.readline()) for i in range(9)]

for i in itertools.combinations(values, 7):
	if sum(i) == 100:
		for j in i:
			print(j)
		break
