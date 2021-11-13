
for _ in range(int(input())):
	k = int(input())
	values = k*[-1]
	fprev, f = 1, 1
	n = 2
	while True:
		fprev, f = f, fprev+f
		if values[f%k] != -1:
			break
		values[f%k] = n
		n += 1
	print(values[f%k])
