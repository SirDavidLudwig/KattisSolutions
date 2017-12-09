from itertools import combinations

w, p = map(int, input().split())
parts = [0] + list(map(int, input().split())) + [w]

sizes = set([comb[1] - comb[0] for comb in combinations(parts, 2)])
print(" ".join([str(size) for size in sorted(list(sizes))])) # Okay, apparently the items in the set aren't sorted...
