from itertools import permutations
import sys

words = []
for line in sys.stdin:
	words = words + line.strip().split()

print("\n".join(sorted(list(set([w[0]+w[1] for w in permutations(words, 2)])))))
