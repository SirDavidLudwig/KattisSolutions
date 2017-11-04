import sys

d  = {'A': 11, 'K': 4, 'Q': 3, 'J': 20, 'T': 10, '9': 14, '8': 0, '7': 0}
nd = {'A': 11, 'K': 4, 'Q': 3, 'J': 2,  'T': 10, '9': 0,  '8': 0, '7': 0}

n, b = sys.stdin.readline().strip().split(" ")

t = 0
for i in range(4*int(n)):
	line = sys.stdin.readline()
	if line[1] == b:
		t += d[line[0]]
	else:
		t += nd[line[0]]

print(t)
