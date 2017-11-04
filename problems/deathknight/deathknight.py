import sys

t = 0
for i in range(int(sys.stdin.readline())):
	if 'CD' not in sys.stdin.readline():
		t += 1
print(t)
