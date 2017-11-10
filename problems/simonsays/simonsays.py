import sys

for i in range(int(sys.stdin.readline())):
	line = sys.stdin.readline().strip()
	if line.startswith("Simon says"):
		print(line[len("Simon says "):])
