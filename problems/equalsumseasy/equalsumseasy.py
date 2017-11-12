from itertools import combinations

def test():
	values = list(map(int, input().split()))
	n = values.pop(0)
	results = {}
	for j in range(1, n+1):
		for s in combinations(values, j):
			r = sum(s)
			if r in results:
				print(" ".join((str(x) for x in s)))
				print(" ".join((str(x) for x in results[r])))
				return
			else:
				results[r] = s
	print("Impossible")

for i in range(int(input())):
	print("Case #%d:" % (i+1))
	test()
