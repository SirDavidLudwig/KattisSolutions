import sys

for i in range(int(input())):
	n = int(input())
	vecA = sorted(list(map(int, input().split())))
	vecB = sorted(list(map(int, input().split())))[::-1]
	total = 0
	for j in range(len(vecA)):
		total += vecA[j]*vecB[j]
	print("Case #%d: %d" % (i+1, total))
