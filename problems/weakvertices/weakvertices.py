from itertools import combinations
import sys

def testWeakness(verts, vert):
	for comb in combinations([v for v in range(len(vert)) if vert[v]], 2):
		if verts[comb[0]][comb[1]]:
			return True
	return False

n = int(input())
while n > -1:
	weak = []
	verts = []
	for i in range(n):
		verts.append(list(map(int, input().split())))
	for i, vert in enumerate(verts):
		if not testWeakness(verts, vert):
			weak.append(i)
	print(" ".join([str(i) for i in weak]))
	n = int(input())
