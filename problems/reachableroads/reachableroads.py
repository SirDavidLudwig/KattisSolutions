import sys

for i in range(int(input())):
	m = int(input())
	am = [[0]*m for i in range(m)]
	for j in range(int(input())):
		a, b = map(int, input().split())
		am[a][b], am[b][a] = 1, 1
	clusters = 0
	remaining = set(range(0, m))
	while remaining:
		clusters += 1
		queue = [remaining.pop()]
		while queue:
			for j, v in enumerate(am[queue.pop(0)]):
				if v and j in remaining:
					queue.append(j)
					remaining.remove(j)
	print(clusters-1)
