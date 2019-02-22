import sys

t = 0
for i in range(int(sys.stdin.readline())):
	line = input().split()
	t += float(line[0])*float(line[1])
print("{0:0.3f}".format(t))
