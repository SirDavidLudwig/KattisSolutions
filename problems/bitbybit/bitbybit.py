n = int(input())
while n:
	bits = ['?']*32
	for i in range(n):
		op = input().strip().split()
		if op[0] == "SET":
			bits[int(op[1])] = 1
		elif op[0] == "CLEAR":
			bits[int(op[1])] = 0
		else:
			i, j = int(op[1]), int(op[2])
			try:
				if op[0] == "AND":
					bits[i] &= bits[j]
				else:
					bits[i] |= bits[j]
			except TypeError:
				v = int(op[0] == "OR")
				bits[i] = v if bits[i] == v or bits[j] == v else '?'


	print("".join([str(b) for b in bits[::-1]]))
	n = int(input())
