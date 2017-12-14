from itertools import permutations

try:
	value = int(input())
	print(min([int("".join(i)) for i in permutations(str(value)) if int("".join(i)) > value]))
except ValueError:
	print(0)
