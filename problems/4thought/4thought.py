import sys

solutions = {}
ops = ['*', '+', '-', '//']
for i in ops:
	for j in ops:
		for k in ops:
			string = "4 {} 4 {} 4 {} 4".format(i, j, k)
			answer = eval(string)
			if answer not in solutions:
				solutions[int(answer)] = "4 {} 4 {} 4 {} 4 = {}".format(i[0], j[0], k[0], answer)

for i in range(int(sys.stdin.readline())):
	try:
		print(solutions[int(sys.stdin.readline())])
	except:
		print("no solution")
