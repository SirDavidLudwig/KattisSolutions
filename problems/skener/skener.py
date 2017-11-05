import sys

R, C, Zr, Zc = map(int, sys.stdin.readline().split())

for i in range(R):
	line = ""
	for char in sys.stdin.readline().strip():
		line += char * Zc
	for j in range(Zr):
		print(line)
