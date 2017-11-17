for i in range(int(input())):
	m = n = 0
	for j, ns in enumerate(input().strip()):
		n = 10*n + int(ns)
		m = max(bin(n).count('1'), m)
	print(m)
