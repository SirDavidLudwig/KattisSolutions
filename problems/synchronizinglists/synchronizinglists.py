import sys

n = int(sys.stdin.readline())
while (n != 0):
	l1 = [int(sys.stdin.readline()) for i in range(n)]
	l2 = sorted([int(sys.stdin.readline()) for i in range(n)])
	l3 = sorted(l1)

	m = {}
	for i in range(n):
		m[l3[i]] = l2[i]

	for i in l1:
		print(m[i])
	print()
	n = int(sys.stdin.readline())
