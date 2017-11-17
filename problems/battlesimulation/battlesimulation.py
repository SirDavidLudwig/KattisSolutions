from itertools import permutations
import re

mapping = {'C': 'C', 'R': 'S', 'B': 'K', 'L': 'H'}
regex = '(' + ")|(".join(["".join(p) for p in permutations("RBL")]) + ')'
line = re.sub(regex, 'C', input().strip())

for char in line:
	print(end=mapping[char])
print()
