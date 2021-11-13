safesum = lambda *v: None if None in v else sum(v)

def safemin(*v):
	try:
		return min(filter(lambda x: x is not None, v))
	except:
		return None

neginf = float('-inf')

# n=#nodes, m=#edges, q=#queries
n, m, q = map(int, input().split())
while n != 0:

	# Adjacency matrix
	dist = [[None]*n for _ in range(n)]
	for i in range(n):
		dist[i][i] = 0
	for _ in range(m):
		u, v, w = map(int, input().split())
		if w < 0:
			dist[u][v] = -1
			continue

		if u == v:
			dist[u][v] = min(dist[u][v], w)
		else:
			dist[u][v] = w

	for k in range(n):
		for i in range(n):
			for j in range(n):
				if i == j and dist[i][j] < 0:
					dist[i][j] = neginf
				else:
					dist[i][j] = safemin(safesum(dist[i][k], dist[k][j]), dist[i][j])

	for _ in range(q):
		a, b = map(int, input().split())
		if dist[a][b] == neginf:
			print("-Infinity")
		elif dist[a][b] == None:
			print("Impossible")
		else:
			print(dist[a][b])
	print()

	n, m, q = map(int, input().split())
