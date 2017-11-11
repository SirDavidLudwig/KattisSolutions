import sys

n = int(sys.stdin.readline())
i = 1
while n != 0:
	animals = {}
	for t in range(n):
		a = sys.stdin.readline().strip().split()[-1].lower()
		if a not in animals:
			animals[a] = 1
		else:
			animals[a] += 1
	print("List {}:".format(i))
	for a in sorted(animals.keys()):
		print(a, '|', animals[a])
	n = int(sys.stdin.readline())
	i += 1
