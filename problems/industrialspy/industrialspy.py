from itertools import combinations, permutations
import sys

def isPrime(n):
	if n == 2 or n == 3:
		return True
	if n & 1 == 0 or n % 3 == 0 or n == 1 or n == 0:
		return False

	i = 5
	w = 2
	while i*i <= n:
		if n % i == 0:
			return False
		i += w
		w = 6 - w
	return True

memoized = {}

for i in range(int(input())):
	total = 0
	line = sorted(input().strip())
	used = set()
	for j in range(len(line), 0, -1):
		for comb in combinations(line, j):
			if comb not in memoized:
				memoized[comb] = 0
				pUsed = set()
				for perm in permutations(comb):
					value = int("".join(perm))
					if value not in pUsed:
						memoized[comb] += isPrime(value)
						pUsed.add(value)
			if int("".join(comb)) not in used:
				total += memoized[comb]
				used.add(int("".join(comb)))
	print(total)
