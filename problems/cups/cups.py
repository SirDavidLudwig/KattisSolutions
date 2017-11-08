import sys

n = int(sys.stdin.readline())
m = {}

for i in range(n):
	t1, t2 = sys.stdin.readline().split(" ")
	if t1.isdigit():
		m[int(t1)//2] = t2.strip()
	else:
		m[int(t2)] = t1.strip()

k = sorted(list(m.keys()))
for i in k:
	print(m[i])
