import sys

for t in range(int(input())):
	e1 = int(input())
	poly1 = tuple(map(int, input().split()))
	e2 = int(input())
	poly2 = tuple(map(int, input().split()))

	result = [0]*(e1+e2+1)
	for i in range(e2+1):
		for j in range(e1+1):
			result[j+i] += poly1[j]*poly2[i]
	print(len(result)-1)
	print(" ".join([str(i) for i in result]))
