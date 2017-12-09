from itertools import combinations
import sys

test = 0
try:
	while True:
		test += 1
		n = int(input())
		ints = [int(input()) for i in range(n)]
		m = int(input())
		queries = [int(input()) for i in range(m)]
		sums = sorted([sum(comb) for comb in combinations(ints, 2)])

		print("Case %d:" % test)
		for query in queries:
			if query <= sums[0]:
				result = sums[0]
			elif query >= sums[-1]:
				result = sums[-1]
			else:
				for i in range(1, len(sums)-1):
					if query <= sums[i]:
						result = sums[i] if sums[i] - query < query - sums[i-1] else sums[i-1]
						break
			print("Closest sum to %d is %d." % (query, result))


except EOFError:
	pass
